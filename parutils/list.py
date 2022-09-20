def list_to_dict(list_in, separator='='):
    """Transforms 'list_in' to a dictionary using the 'separator'"""

    out = {}
    for elt in list_in:
        e = elt.split(separator)
        key = e[0].strip()
        value = elt[elt.find(separator) + 1:].strip()
        out[key] = value
    return out
