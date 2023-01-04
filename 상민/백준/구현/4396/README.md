### 풀이 방식

### 변수

```cpp
char solution[N][N]; // 폭탄이 표시된 해답
char board[N][N]; // 사용자가 버튼을 누른지 여부
vector<tuple<int, int>> bombLocation; // 폭탄 위치 튜플로 저장 (폭탄건드릴 시 표시하기 위해)
bool isExploded; // 폭탄을 건드렸는지 여부
```

### 폭탄 하나라도 건드리면 전부 다 표시

```cpp
if (solution[row][col] == '*') {
    isExploded = true; // 이게 참이되면 폭탄 위치 다 표시
}
```

### 반복문 돌면서 주변 폭탄을 확인

```cpp
board[row][col] = '0';
for (int y = -1; y<=1; y++) {
    for (int x = -1; x<=1; x++) {
        // 낭떠러지 필터링
        if (row + y < 0 || row + y >= N || col + x < 0 || col + x >= N) {
            continue;
        }
        if (solution[row+y][col+x] == '*') {
            board[row][col] += 1;
        }
    }
}
```

![스크린샷 2023-01-04 오전 12.10.54.png](https://user-images.githubusercontent.com/109147915/210386298-0e8af65c-1f9a-4013-bcde-77545bf7f229.png)
