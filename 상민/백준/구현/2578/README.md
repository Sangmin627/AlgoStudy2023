# 풀이 방식

### 변수

```cpp
int board[5][5]; // 내 빙고판
int horizontal[5]; //가로 라인 당 몇개 지우고 남은지
int vertical[5]; // 세로 라인 당 몇개 지우고 남은지
int leftHeadedDiagonal; //좌상단우하단 대각선
int rightHeadedDiagonal; //좌하단 우상단 대각선
```

### 반복문 돌면서 사회자가 부른 숫자 찾고나서

```cpp
// 가로 라인 지우고 0되면 라인 세기
lineCount = ((horizontal[row] -= 1) == 0) ? (lineCount + 1) : lineCount;
// 세로 라인 지우고 0되면 라인 세기
lineCount = ((vertical[col] -= 1) == 0) ? (lineCount + 1) : lineCount;
if (row == col) { // 좌상우하 대각선 지우고 0되면 라인 세기
    lineCount = ((leftHeadedDiagonal -= 1) == 0) ? (lineCount + 1) : lineCount;
}
if (row + col == 4) { //좌하우상 대각선 지우고 0되면 라인 세기
    lineCount = ((rightHeadedDiagonal -= 1) == 0) ? (lineCount + 1) : lineCount;
}
```

![스크린샷 2023-01-03 오후 10.48.08.png](https://user-images.githubusercontent.com/109147915/210377986-c1b52035-a088-46d9-839c-ff6dc4d13629.png)
