#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int n; cin>>n;
    int list[10001];
    int memo[10001][3]; //몇번 연속으로 밟은지에 따라 각자의 최대값
    // 0: 나를 포함안하는애 1나를 포함해서 연속1 2 나를포함해서 연속 2번째
    for (int i = 1; i<=n; i++) {
        cin>>list[i];
    }

    memo[1][1] = list[1];
    memo[1][0] = list[0];
    memo[1][2] = list[0];
    for (int i = 1; i<=n; i++) {
        memo[i][1] = memo[i-1][0] + list[i]; // 나포함 연속1
        memo[i][0] = max(memo[i-1][1], memo[i-1][2]); // 나를 미포함
        memo[i][2] = memo[i-1][1] + list[i]; //나포함 연속2
    }

    cout<<max(memo[n][1], memo[n][2]);
    return 0;
}
