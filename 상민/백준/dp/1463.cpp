#include <iostream>
#include <limits.h>
#include <cmath>
using namespace std;
int main() {

    int N; cin>>N;

    int memo[1000001];
    memo[1] = 0;
    for (int i = 2; i<=N; i++) {

        int minimum = INT_MAX;
        if (i%3 == 0) {
            minimum = min(minimum, memo[i/3] + 1);
        }
        if (i%2 == 0) {
            minimum = min(minimum, memo[i/2] + 1);
        }

        minimum = min(minimum,  memo[i-1] + 1);

        memo[i] = minimum;
    }

    cout<<memo[N];

    return 0;
}
