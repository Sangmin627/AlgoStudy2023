def solution(files):
    answer = []
    tmp = []

    for file in files:
        h, n, t = "", "", ""
        hflag, nflag = True, True

        for f in file:
            if not f.isdigit():
                if hflag:
                    h += f
                else:
                    nflag = False

            if f.isdigit() and nflag:
                hflag = False
                if len(n) > 5:
                    nflag = False
                else:
                    n += f

            if not hflag and not nflag:
                t += f
        tmp.append([h, n, t])

    tmp.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for i in tmp:
        answer.append("".join(i))

    return answer