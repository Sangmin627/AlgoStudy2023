#include <iostream>
#include <algorithm>
using namespace std;
bool compare(int a, int b) {
    return a>b;
}
int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N; cin>>N;
    int list[N];
    for (int i = 0; i<N; i++) {
        cin>>list[i];
    }

    sort(list, list+N, compare);

    int maximum = -1;
    for (int i = 0; i<N; i++) {
        maximum = max(maximum, (i+1)*list[i]);
    }

    cout<<maximum;


    return 0;
}
