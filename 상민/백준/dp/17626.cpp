#include <iostream>
#include <cmath>
#include <limits.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int list[50001];

    list[0] = 0;
    list[1] = 1;

    int target; cin>>target;

    /*
     0 = 0
     1 = 1  1
     2 = 1+1    2
     3 = 1+1+1  3
     4 = 2*2   1
     5 = 2*2+1  2
     6 = 2*2+1+1    3
     7 = 2*2+1+1+1  4
     8 = 2*2+2*2    2
     9 = 3*3    1
     */

    for (int i = 2; i<=target; i++) {

        int minimum = INT_MAX;

        for (int j = 1; j<=sqrt(i); j++) {
            minimum = min(minimum, list[i-j*j]);
        }

        list[i] = minimum + 1;
    }

    cout<<list[target];
    return 0;
}
