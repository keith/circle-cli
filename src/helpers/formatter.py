def output_rows(rows):
    max_lengths = [0] * len(rows[0])
    for row in rows:
        for i, column in enumerate(row):
            max_lengths[i] = max(len(unicode(column)), max_lengths[i])

    for row in rows:
        string = ""
        for i, column in enumerate(row):
            pad = (max_lengths[i] - len(unicode(column))) * " "
            string += unicode(column) + pad + "\t"
        print(string)
