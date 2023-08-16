### 풀이 방식

### 변수

```cpp
map<char, tuple<int, int>> board; // 키값의 y,x 인덱스를 튜플로 저장하는 맵
int vowelIndex[3] // 자음, 모음을 구분하는 인덱스 (줄별로 유지중)
int leftY, leftX; //왼손의 좌표
int rightY, rightX; //오른손의 좌표
```

### 로직

```cpp
for (int i = 0; i<word.size(); i++) {
        char targetY = get<0>(board[word[i]]);
        char targetX = get<1>(board[word[i]]);

        // vowelIndex에서 자음, 모음 여부에 따라 왼손, 오른손으로 찍는게 나뉨
        if (vowelIndex[targetY] <= targetX) { // 오른손으로 찍어야함
            totalTime += (abs(rightY - targetY) + abs(rightX - targetX));
            rightY = targetY;
            rightX = targetX;
        }
        else { // 왼손으로 찍어야함
            totalTime += (abs(leftY - targetY) + abs(leftX - targetX));
            leftY = targetY;
            leftX = targetX;
        }

        totalTime += 1;

    }
```
