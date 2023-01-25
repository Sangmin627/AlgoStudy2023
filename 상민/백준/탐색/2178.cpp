#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int N, M;
int yer[] = {-1, 0, 1, 0};
int xer[] = {0, -1, 0, 1};

char map[101][101];
bool isVisited[101][101];

int bfs(int initY, int initX) {
    queue<tuple<int, int>> q;
    q.push(make_tuple(initY, initX));
    isVisited[initY][initX] = true;

    int count = 1;
    bool flag = false;
    while(!q.empty()) {
        for (int c = q.size()-1; c>=0; c--) {
            int y = get<0>(q.front());
            int x = get<1>(q.front());
            q.pop();

            if (y == N-1 && x == M-1) {
                flag = true;
                break;
            }

            for (int i = 0; i<4; i++) {
                int newY = y+yer[i];
                int newX = x+xer[i];
                if (newY < 0 || newY >= N || newX < 0 || newX >= M) {
                    continue;
                }
                if (map[newY][newX] == '0') {
                    continue;
                }
                if (isVisited[newY][newX]) {
                    continue;
                }
                isVisited[newY][newX] = true;

                q.push(make_tuple(newY, newX));
            }
        }
        if (flag) {
            break;
        }
        count+=1;
    }
    return count;
}

int main() {
    cin>>N>>M;

    for (int i = 0; i<N; i++) {
        for (int j = 0; j<M; j++) {
            cin>>map[i][j];
        }
    }

    // 0,0에서 N-1, M-1까지
    cout<<bfs(0,0);

    return 0;
}
