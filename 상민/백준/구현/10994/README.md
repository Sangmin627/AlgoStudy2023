### 풀이 방식

### 변수

```cpp
int center = 2*N-1; // 중앙 인덱스
int len = 2*center-1; // 가장 바깥놈 길이
char result[len+1][len+1]; // 프린트할거 담는곳
```

### 로직

```cpp
for (int n = 1; n<=N; n++) { 
                // n으로 만든 홀수만큼 상하좌우 길이를 갖는다
        int odd = 2*n-1;

                // 각 n이 그릴 사각형의 최소, 최대 인덱스를 구해서 그려줌
        int min = center - (odd-1);
        int max = center + (odd-1);

        for (int i = min; i<=max; i++) {
            for (int j = min; j<=max; j++) {
                                // 테두리만 별찍어주기
                if (i == min || i == max || j == min || j == max) {
                    result[i][j] = '*';
                }
            }
        }
    }
```
