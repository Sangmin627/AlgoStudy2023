#include <iostream>
#include <limits.h>
#include <algorithm>
using namespace std;
int main() {

    int n; cin>>n;

    int memo[100001];
    memo[0] = 0;

    for (int i = 1; i<=n; i++) {
        int result;
        int a = INT_MAX;
        int b = INT_MAX;

        if (i >= 2 && memo[i-2] != -1) {
            a = memo[i-2] + 1;
        }
        if (i>=5 && memo[i-5] != -1) {
            b = memo[i-5] + 1;
        }
        result = min(a,b);

        memo[i] = (result != INT_MAX) ? result : -1;
    }

    cout<<memo[n];

    return 0;
}
