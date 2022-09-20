import parutils.file as fl
import parutils.string as st


def extract_doc(in_dirs, out_path):
    """Extracts all Python doc ('# comments included) present in the 'in_dir'
    directories (can be usefull for spell check)
    """

    out = []
    for in_dir in in_dirs:
        extract_doc_from_dir(in_dir, out)

    fl.save_list(out, out_path)
    fl.startfile(out_path)


def extract_doc_from_dir(in_dir, out):
    file_list = fl.list_files(in_dir, walk=True, only_list=['*.py'])
    for i, file in enumerate(file_list, 1):
        extract_doc_from_file(file, out)


def extract_doc_from_file(path, out):
    out.append(path)
    out.append(st.extend_str('', '-', 100))
    x = fl.load_txt(path)
    description = False
    n_written = 0
    for i, line in enumerate(x):
        append = False
        if '#' in line or st.like(line, '*"""*"""*'):
            append = True
        elif '"""' in line and description is False:
            description = True
            append = True
        elif '"""' in line and description is True:
            description = False
            append = True
        elif description is True:
            append = True
        if append:
            line = line.strip()
            out.append(line)
            n_written += 1

    if n_written > 0:
        out.append(st.extend_str('', '-', 100))
        out.append('')
        out.append('')
    else:
        del out[-2:]
