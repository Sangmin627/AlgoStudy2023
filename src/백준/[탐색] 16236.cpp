#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int N;
int map[20][20];
int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

bool visited[20][20]; //사이즈, 먹은수, Y, X

class Shark {
public:
    int y,x,cnt,size, time;
    Shark(int y, int x, int size, int cnt, int time) {
        this->y=y;
        this->x=x;
        this->size=size;
        this->cnt=cnt;
        this->time = time;

    }
};
bool bfs();

Shark shark1(0,0,2,0, 0);


int main() {

    cin>>N;
    for (int i = 0; i<N; i++) {
        for (int j = 0; j<N; j++) {
            cin>>map[i][j];
            if(map[i][j] == 9) {
                map[i][j] = 0;
                shark1.y = i;
                shark1.x = j;
            }
        }
    }

    bool flag = true;

    while(flag) {
        for(int i=0; i<20; i++)  memset(visited[i], false, sizeof(visited[i]));
        flag = bfs();
    }

    cout<<shark1.time;

    return 0;
}


bool bfs() {
    int time = 0;

    pair<int, int> dest;
    int size = shark1.size;
    int cnt = shark1.cnt;
    queue<pair<int, int>> queue1;
    queue1.push(make_pair(shark1.y, shark1.x));
    visited[shark1.y][shark1.x] = true;

    bool flag;
    while(!queue1.empty()) {
        flag = false;
        dest = make_pair(-1,-1);
        for (int i = queue1.size(); i>0; i--) {
            int y = queue1.front().first;
            int x = queue1.front().second;
            queue1.pop();

            for (int j = 0; j<4; j++) {
                int Y = y+dy[j];
                int X = x+dx[j];
                if(X==-1||X==N||Y==-1||Y==N) continue;
                if(map[Y][X]>size) continue;
                if(visited[Y][X]) continue;
                visited[Y][X] = true;

                if(map[Y][X] == size || map[Y][X] == 0) { //이동
                    queue1.push(make_pair(Y,X));
                }

                else { //먹잇감 발견
                    if(dest.first != -1 && dest.second == -1) { //만약 이미 같은 time 내에서 먹이를 발견했다면
                        if(Y < dest.first) {
                            dest = make_pair(Y,X);
                        }
                        else if(Y == dest.first && X < dest.second) {
                            dest = make_pair(Y,X);
                        }
                    }
                    else {//현재 time에 먹이를 발견 못한 상태라면
                        dest = make_pair(Y,X);
                    }
                    flag = true;
                }
            }

        }
        time++;
        if(flag) { //먹잇감을 발견했다면
            if(cnt+1 == size) { //먹은 수와 크기가 일치하면 사이즈 증가
                shark1.size+=1;
                shark1.cnt = 0;
                shark1.y = dest.first;
                shark1.x = dest.second;
            }
            else { //먹은 수 + 1
                shark1.cnt+=1;
                shark1.y = dest.first;
                shark1.x = dest.second;
            }
            map[dest.first][dest.second] = 0;
            shark1.time += time;
            return true;
        }
    }

    return false;

}
