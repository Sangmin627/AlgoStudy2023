import sys
input = sys.stdin.readline

vowel = ['a','e','i','o','u']

def con1(w):
    for i in range(len(w)):
        if w[i] in vowel:
            return True
    return False

def con2(w):
    if len(w) >= 3:
        for i in range(1, len(w)-1):
            if w[i-1] in vowel and w[i] in vowel and w[i+1] in vowel:
                return False
            if w[i-1] not in vowel and w[i] not in vowel and w[i+1] not in vowel:
                return False
    return True

def con3(w):
    if len(w) >= 2:
        for i in range(1, len(w)):
            if w[i-1] == w[i]:
                if w[i-1] == 'e' or w[i-1] == 'o':
                    continue
                else:
                    return False
    return True


while True:
    flag = False
    w = input().rstrip()
    if w == "end":
        break

    if con1(w) and con2(w) and con3(w):
        print("<" + w + "> is acceptable.")
        continue
    print("<" + w + "> is not acceptable.")


