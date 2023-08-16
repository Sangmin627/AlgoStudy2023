#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<int> graph[100001];
bool isVisited[100001];
int parent[100001];
void dfs(int n) {
    for (int i = 0; i<graph[n].size(); i++) {
        int tmp = graph[n][i];
        if (!isVisited[tmp]) {
            isVisited[tmp] = true;
            parent[tmp] = n;
            dfs(tmp);
        }
    }
}

void bfs(int n) {
    queue<int> q;
    q.push(n);
    isVisited[n] = true;

    while(!q.empty()) {
        int target = q.front();
        q.pop();
        for (int i = 0; i<graph[target].size(); i++) {
            int tmp = graph[target][i];
            if (!isVisited[tmp]) {
                isVisited[tmp] = true;
                q.push(tmp);
                parent[tmp] = target;
            }
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N; cin>>N;

    for (int i = 0; i<N-1; i++) {
        int a,b; cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    isVisited[1] = true;
    bfs(1);

    for (int i = 2; i<=N; i++) {
        cout<<parent[i]<<"\n";
    }

    return 0;
}
