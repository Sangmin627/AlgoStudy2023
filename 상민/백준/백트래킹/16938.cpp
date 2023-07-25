#include <iostream>
#include <limits.h>
using namespace std;

int N; //총 문제
int L; //합 최소
int R; //합 최대
int X; //가장 쉬운, 어려운 문제의 차이의 최대값
int A[16];

int ans = 0;

void dfs(int idx, int min, int max, int count, int sum) {

    int a = A[idx];
    int newMin = (a < min) ? a : min;
    int newMax = (a > max) ? a : max;
    int newSum = sum += a;
    int newCount = count + 1;


    if (L <= newSum && newSum <= R && newMax - newMin >= X && newCount >= 2) {
        ans += 1; // 추가 ㄱㄱ
    }

    for (int i = idx + 1; i<N; i++) {
        dfs(i, newMin, newMax, newCount, newSum);
    }
}

int main() {


    cin>>N>>L>>R>>X;
    // 정렬 한번 하고 타는게 맞겠지?
    for (int i = 0; i<N; i++) {
        cin>>A[i];
    }

    for (int i = 0; i<N; i++) {
        dfs(i, INT_MAX, INT_MIN, 0, 0);
    }

    cout<<ans;


    return 0;
}
