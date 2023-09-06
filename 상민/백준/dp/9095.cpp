#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int T, n; cin>>T;

    int memo[12];

    memo[1] = 1;
    memo[2] = 2;
    memo[3] = 4;

    for (int i = 4; i<=11; i++) {
        memo[i] = memo[i-3] + memo[i-2] + memo[i-1];
    }

    for (int i = 0; i<T; i++) {
        cin>>n;
        cout<<memo[n]<<"\n";
    }
    return 0;
}
