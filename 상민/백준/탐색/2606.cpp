#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int N; cin>>N;

    vector<int> graph[101];
    bool isVisited[101];

    int L; cin>>L;

    for (int i = 0; i<L; i++) {
        int a, b; cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    queue<int> Queue;
    Queue.push(1);
    isVisited[1] = true;

    int total = 0;
    while(!Queue.empty()) {
        int target = Queue.front();
        Queue.pop();
        for (int i = 0; i<graph[target].size(); i++) {
            int tmp = graph[target][i];
            if (!isVisited[tmp]) {
                isVisited[tmp] = true;
                Queue.push(tmp);
                total += 1;
            }
        }
    }

    cout<<total;
    return 0;
}
