def solution(operations):
    arr = []
    for o in operations:
        if o[0] == "I":
            arr.append(int(o[2:]))
        elif o == "D -1" and arr:
            arr.sort()
            arr.pop(0)
        elif o == "D 1" and arr:
            arr.sort(reverse=True)
            arr.pop(0)

    if not arr:
        return [0, 0]
    else:
        arr.sort()
        return [arr[-1], arr[0]]