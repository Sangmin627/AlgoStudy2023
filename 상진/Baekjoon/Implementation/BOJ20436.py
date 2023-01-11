startLeft, startRight = input().split()
keyBoards = list(map(str, input()))

left = {'q':(0,2), 'w':(1,2), 'e':(2,2), 'r':(3,2), 't':(4,2),
        'a':(0,1), 's':(1,1), 'd':(2,1), 'f':(3,1), 'g':(4,1),
        'z':(0,0), 'x':(1,0), 'c':(2,0), 'v':(3,0)}

right = {'y':(5,2),'u':(6,2),'i':(7,2),'o':(8,2),'p':(9,2),
         'h':(5,1),'j':(6,1),'k':(7,1),'l':(8,1),
         'b':(4,0),'n':(5,0),'m':(6,0)}

answer = 0
lastLeft, lastRight = startLeft, startRight
lastLeftIndex, lastRightIndex = left.get(startLeft), right.get(startRight)

for cur in keyBoards:
    if cur in left.keys():
        start, end = left.get(lastLeft), left.get(cur)
        answer += abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1
        lastLeft, lastLeftIndex = cur, left.get(cur)
    elif cur in right.keys():
        start, end = right.get(lastRight), right.get(cur)
        answer += abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1
        lastRight, lastRightIndex = cur, right.get(cur)

print(answer)