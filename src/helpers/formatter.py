def output_rows(rows):
    if not rows:
        return ""

    max_lengths = [0] * len(rows[0])
    for row in rows:
        for i, column in enumerate(row):
            max_lengths[i] = max(len(str(column)), max_lengths[i])

    output = ""
    for row in rows:
        string = ""
        for i, column in enumerate(row):
            pad = (max_lengths[i] - len(str(column))) * " "
            string += str(column) + pad + "\t"
        output += string.strip() + "\n"

    return output
