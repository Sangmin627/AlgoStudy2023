#include <iostream>
using namespace std;
int main() {
    int N; cin>>N;

    int center = 2*N-1;
    int len = 2*center-1;

    char result[len+1][len+1];
    for (int i = 1; i<=len; i++) {
        for (int j = 1; j<=len; j++) {
            result[i][j] = ' ';
        }
    }

    for (int n = 1; n<=N; n++) {
        int odd = 2*n-1;

        int min = center - (odd-1);
        int max = center + (odd-1);

        for (int i = min; i<=max; i++) {
            for (int j = min; j<=max; j++) {
                if (i == min || i == max || j == min || j == max) {
                    result[i][j] = '*';
                }
            }
        }
    }

    for (int i = 1; i<=len; i++) {
        for (int j = 1; j<=len; j++) {
            cout<<result[i][j];
        }
        cout<<endl;
    }


    return 0;
}
