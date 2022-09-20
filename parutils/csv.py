from . import file
from .logging import log
from .logging import log_print

SEPARATOR = ';'


def get_csv_fields_dict(in_path):
    """Returns a dictionary whose keys are the csv fields of the 'in_path' file
    and elements are the columns index.
    """
    from . import header

    fields = {}
    line_list = header.get_header(in_path, True)
    for i, elt in enumerate(line_list):
        fields[elt] = i

    return fields


def load_csv(in_path):
    """Loads a csv file and returns a list whose elements correspond to the
    lines of the 'in_path' file.
    Each element is also a list whose elements correspond to the csv fields.
    """

    out_list = []
    with open(in_path, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            line_list = csv_to_list(line)
            out_list.append(line_list)

    return out_list


def csv_to_list(line_in):
    """Converts a csv line to a list using SEPARATOR as separator"""

    return line_in.strip('\n').split(SEPARATOR)


def save_csv(array_in, out_path, mode='w'):
    """Saves a list to a csv file

    - mode: mode for the open methode.
    """
    import os.path as p

    file.mkdirs(p.dirname(out_path))
    with open(out_path, mode, encoding='utf-8') as out_file:
        for row in array_in:
            write_csv_line(row, out_file)


def write_csv_line(row, out_file):
    """Writes a line to a csv file

    - row: can be either a list of the csv fields or a csv string
    """

    if isinstance(row, str):
        line_out = row
    else:
        line_out = SEPARATOR.join(row)
    line_out += '\n'
    out_file.write(line_out)


def csv_clean(s):
    """Cleans a csv field by removing csv separators and new line characters"""

    out = s.replace('\r', '')
    out = out.replace('\n', '')
    out = out.replace(SEPARATOR, '')
    return out


def get_header(in_path, csv=False):
    """Returns the header of a file

    - csv: if True, the returned header is a list containing each csv field
    """
    from .csv import csv_to_list

    with open(in_path, 'r', encoding='utf-8') as in_file:
        header = in_file.readline().strip('\n')

    if csv:
        header = csv_to_list(header)

    return header


def gen_header(in_path, sep, field='FIELD', last_field='', out_path=''):
    """If the in_path file has no header, this function generates one looking
    like this : FIELD_1;FIELD_2;...;FIELD_N; last_field where N is the number
    of columns of the csv file. If last_field == '' it is not appended.
    If an out_path is passed in, a file is created with the generated header
    (or with the existing one is the in_path file has one)
    """

    if has_header(in_path):
        header = get_header(in_path)
    else:
        first_line = get_header(in_path, True)
        header = field + "_1"
        if len(first_line) > 1:
            counter = 1
            for elt in first_line[1:]:
                counter += 1
                header = f'{header}{sep}{field}_{counter}'

    if last_field:
        header = header + sep + last_field

    if out_path:
        with open(out_path, 'w', encoding='utf-8') as out_file:
            out_file.write(header + '\n')

    return header


def has_header(inp):
    """Returns True if inp has a header (inp can be a file path or a list).
    To do so, it looks at the first elements of the two first lines. If they
    are of same length then we consider that inp has no header and conversely.
    Note that this function should be used with caution as it can not be fully
    reliable.
    """
    from .csv import csv_to_list

    out = True
    if isinstance(inp, str):
        ar = []
        with open(inp, 'r', encoding='utf-8') as in_file:
            ar.append(csv_to_list(in_file.readline()))
            ar.append(csv_to_list(in_file.readline()))
    else:
        ar = inp

    if not ar:
        return False
    if len(ar) == 1:
        return True
    if isinstance(ar[0], str):
        if len(ar[0]) == len(ar[1]):
            out = False
    else:
        if len(ar[0][0]) == len(ar[1][0]):
            out = False

    return out


def check_header(in_path):
    """Logs an error message and raises an exception if the in_path file has no
    header (relies on the has_header function).
    """
    E_MH = "Missing header (first elements of line 1 and 2 must be of different length)"

    if not has_header(in_path):
        s = f"Error: the input file {in_path} must have a header"
        log(s)
        s = "Make sure the first elements of the first two lines are of different lengths"
        log_print(s)
        raise Exception(E_MH)
