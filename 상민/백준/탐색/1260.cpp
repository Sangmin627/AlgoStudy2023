#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
using namespace std;

int N, M, V;
vector<int> graph[1001];
bool isVisited[1001];


void dfs(int n) {
    cout<<n<<" ";
    for (int i = 0; i<graph[n].size(); i++) {
        int tmp = graph[n][i];
        if (!isVisited[tmp]) {
            isVisited[tmp] = true;
            dfs(tmp);
        }
    }
}

void bfs(int n) {
    queue<int> Queue;
    isVisited[n] = true;
    Queue.push(n);

    while(!Queue.empty()) {
        int target = Queue.front();
        Queue.pop();

        cout<<target<<" ";

        for (int i = 0; i<graph[target].size(); i++) {
            int tmp = graph[target][i];
            if (!isVisited[tmp]) {
                isVisited[tmp] = true;
                Queue.push(tmp);
            }
        }
    }
}
int main() {
    cin>>N>>M>>V;

    for (int i = 0; i<M; i++) {
        int a, b; cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for (int i = 1; i<=N; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    isVisited[V] = true;
    dfs(V);

    cout<<endl;
    memset(isVisited, false, 1001);
    bfs(V);
    return 0;
}
