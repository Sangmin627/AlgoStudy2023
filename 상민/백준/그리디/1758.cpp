#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
bool compare(int a, int b) {
    return a>b;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 마이너스가 되는 놈은 앞에 세워야함. 하나라도 버리는게 이득.

    int N; cin>>N;
    int list[N];
    for (int i = 0; i<N; i++) {
        cin>>list[i];
    }
    sort(list, list+N, compare);

    ll sum = 0;
    for (int i = 0; i<N; i++) {
        int tmp = list[i] - i;
        if (tmp <= 0) {
            break;
        }
        sum += tmp;
    }


    cout<<sum;

    return 0;
}
