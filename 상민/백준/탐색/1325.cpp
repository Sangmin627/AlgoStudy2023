#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

vector<int> graph[10001];
bool isVisited[10001];
int isHackable[10001];

//int dfs(int n) {
//    int ret = 1;
//    for (int i = 0; i<graph[n].size(); i++) {
//        int tmp = graph[n][i];
//        if (!isVisited[tmp]) {
//            isVisited[tmp] = true;
//            ret += dfs(tmp);
//        }
//    }
//
//    return ret;
//}

int bfs(int n) {
    queue<int> q;
    q.push(n);
    isVisited[n] = true;
    int ret = 1;
    while(!q.empty()) {
        int target = q.front();
        q.pop();
        for (int i = 0; i<graph[target].size(); i++) {
            int tmp = graph[target][i];
            if (!isVisited[tmp]) {
                isVisited[tmp] = true;
                q.push(tmp);
                ret += 1;
            }
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N,M; cin>>N>>M;
    for (int i = 0; i<M; i++) {
        int a,b; cin>>a>>b;
        graph[b].push_back(a);
    }

    int Max = -1;
    for (int i = 1; i<=N; i++) {
        memset(isVisited, false, N+1);
        isHackable[i] = bfs(i);
        Max = max(Max, isHackable[i]);
    }

    for (int i = 1; i<=N; i++) {
        if (isHackable[i] == Max) {
            cout<<i<<" ";
        }
    }

    return 0;
}