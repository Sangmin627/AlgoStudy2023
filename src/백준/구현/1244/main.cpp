#include <iostream>
#include <algorithm>
using namespace std;
int main() {

    int N; cin>>N;
    int switchList[N+1];
    int S;

    for (int i = 1; i<=N; i++) {
        cin>>switchList[i];
    }
    cin>>S;

    for (int i = 0; i<S; i++) {
        int gender; cin>>gender;
        int n; cin>>n;

        if (gender == 1) {
            for (int j = 1; j<=N; j++) {
                if ((j)%n == 0) {
                    switchList[j] = !switchList[j];
                }
            }
        } else {
            int back = N-n;
            int front = n-1;
            int limit = min(back, front);

            switchList[n] = !switchList[n];
            for (int j = 1; j<=limit; j++) {
                if (switchList[n-j] != switchList[n+j]) {
                    break;
                }
                switchList[n-j] = !switchList[n-j];
                switchList[n+j] = !switchList[n+j];
            }
        }
    }

    for (int i = 1; i<=N; i++) {
        cout<<switchList[i]<<" ";
        if (i%20 == 0) {
            cout<<endl;
        }
    }

    return 0;
}
