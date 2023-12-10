#include <iostream>
#include <stack>
using namespace std;
int main() {

    cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);
    int N, K; cin>>N>>K;
    stack<char> s;
    char c[500001];

    for (int i = 0; i<N; i++) {
        cin>>c[i];
    }

    int erased = 0;

    //만약 다 못지우면? 스택에 남은 놈들로 다시 돌릴수있나?
    for (int i = 0; i<N; i++) {
        while(!s.empty() && s.top() < c[i] && erased < K) { //만약 지울만큼 지우면? 멈춰야함
            s.pop();
            erased ++;
        }
        s.push(c[i]);
    }

    for (int i = erased; i<K; i++) {
        s.pop();
    }


    N = s.size();

    // erase가 남으면? 뒤에서 지우자

    while(!s.empty()) {
        c[s.size() - 1] = s.top();
        s.pop();
    }
    c[N] = '\0';


    cout<<c;

    // 앞부터 말고 뒤부터 지워야하나??? 어케?

    return 0;
}
