#include <iostream>
using namespace std;

int main() {

    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int memo[1010];
    memo[1] = 1;
    memo[2] = 2;

    int n; cin>>n;


    for (int i = 3; i<=n; i++) {
        memo[i] = (memo[i-2] + memo[i-1])%10007;
    }

    cout<<memo[n];
    return 0;
}
