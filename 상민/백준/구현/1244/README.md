### 풀이 방식

### 변수

```cpp
int switchList[N+1]; // 스위치의 상태를 담는 배열
```

### 남자

```cpp
돌면서 배수 인덱스인 스위치 상태 변경
for (int j = 1; j<=N; j++) {
    if ((j)%n == 0) {
        switchList[j] = !switchList[j];
    }
}
```

### 여자

```cpp
int back = N-n; //뒤에 나아갈 수 있는 수
int front = n-1; //앞에 나아갈 수 있는 수
int limit = min(back, front); // 둘중 작은거

switchList[n] = !switchList[n]; //가운데 먼저 바꾸고
for (int j = 1; j<=limit; j++) { // 돌면서 양쪽 일치하면 상태변경
    if (switchList[n-j] != switchList[n+j]) {
        break;
    }
    switchList[n-j] = !switchList[n-j];
    switchList[n+j] = !switchList[n+j];
}
```

![스크린샷 2023-01-04 오전 12.58.18.png](https://user-images.githubusercontent.com/109147915/210393971-eea97676-cdf4-4fa3-80d3-b9018b651237.png)
