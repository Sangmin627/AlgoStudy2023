# 풀이 방식

### 변수

```cpp
int JoonMoney; // 준석이가 가진 현금
int SungMoney; // 성민이가 가진 현금
int JoonCount = 0; // 준석이가 가진 주
int SungCount = 0; // 성민이가 가진 주
```

### 풀 매수 로직

```cpp
int SungCurCount = SungMoney / jooga;
SungMoney -= SungCurCount * jooga;
SungCount += SungCurCount;
```

### 풀 매도 로직

```
SungMoney += SungCount * jooga;
SungCount = 0;
```

### 과정

- 준석이는 무조건 풀매수 로직만 한다
- 성민이는 경우에 따라 풀매수, 풀매도를 함
    - 이전 주가와 현재 주가 비교를 위해 이전 주가를 저장하는 `befJooga` 변수를 선언하여 현재 주가와 비교
    - 이전과 현재를 비교하여 주가가 상승한 경우를 1, 동일한 경우를 0, 하락한 경우를 -1 로 하는 `state` 라는 변수를 유지함.
    - `state`가 유지된 횟수를 기록하는 `stateCounter` 변수를 선언하여 `state`가 바뀐 경우는 1로 초기화, 유지되는 경우는 += 1 해준다.
    - `stateCounter`의 값이 3 이상일 경우 `state`에 따라 풀매수, 풀매도 로직을 실행
    

![스크린샷 2023-01-03 오후 10.48.08.png](https://user-images.githubusercontent.com/109147915/210370111-d35d66db-5430-4a72-b33c-0fcdbce30acf.png)
