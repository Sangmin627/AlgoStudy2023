### 풀이 방식

### 변수

```cpp
int memo[100001]; // 최소 잔돈 개수를 저장할 메모이제이션, memo[0] = 0으로 시작하자
```

### 로직

```cpp
for (int i = 1; i<=n; i++) {
        int result;
        int a = INT_MAX; // 2원 뺀값의 최소 개수
        int b = INT_MAX; // 5원 뺀값의 최소 개수

        if (i >= 2 && memo[i-2] != -1) {
            a = memo[i-2] + 1;
        }
        if (i>=5 && memo[i-5] != -1) {
            b = memo[i-5] + 1;
        }
        result = min(a,b);

        memo[i] = (result != INT_MAX) ? result : -1;
    }
```

![스크린샷 2023-01-11 오전 8.12.32.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4caf35b1-a3bf-4baf-8a85-4c6fc22c18c8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-01-11_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_8.12.32.png)

이걸 누가 그리디라고 하노?
