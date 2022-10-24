def line_count(line):
    line_split = line.split()
    u = 0
    for i in line_split:
        u_local = 0
        for k in i:
            if k.isupper():
                u_local += 1
        if u_local > len(i) - u_local:
            u += 1
    fin = str(int(u / len(line_split) * 100)) + '%'
    return fin