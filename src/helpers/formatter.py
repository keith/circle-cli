def _safe_encode(value):
    try:
        return str(value)
    except UnicodeEncodeError:
        return value


def output_rows(rows):
    if not rows:
        return ""

    max_lengths = [0] * len(rows[0])
    for row in rows:
        for i, column in enumerate(row):
            max_lengths[i] = max(len(_safe_encode(column)), max_lengths[i])

    output = ""
    for row in rows:
        string = ""
        for i, column in enumerate(row):
            pad = (max_lengths[i] - len(_safe_encode(column))) * " "
            string += _safe_encode(column) + pad + "\t"
        output += string.strip() + "\n"

    return output
