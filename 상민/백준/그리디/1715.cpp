#include <iostream>
#include <queue>
#include <vector>
using namespace std;
typedef long long ll;

int main() {

    cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);

    priority_queue<ll, vector<ll>, greater<ll>> q;
    int N;
    cin>>N;
    for (int j = 0; j<N; j++) {
        int a; cin>>a;
        q.push(a);
    }

    ll sum = 0;

    while(q.size() > 1) {
        ll a = q.top();
        q.pop();
        ll b = q.top();
        q.pop();

        sum += (a+b);

        q.push(a+b);
    }

    cout<<sum<<"\n";

    return 0;
}
