#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int main() {

    int N; cin>>N;
    char solution[N][N];
    char board[N][N];
    vector<tuple<int, int>> bombLocation;

    // ., *가 나온 해답지
    for (int i = 0; i<N; i++) {
        for (int j = 0; j<N; j++) {
            cin>>solution[i][j];
            if (solution[i][j] == '*') {
                bombLocation.push_back(make_tuple(i, j));
            }
        }
    }

    // 사용자가 버튼 누른 보드
    for (int i = 0; i<N; i++) {
        for (int j = 0; j<N; j++) {
            cin>>board[i][j];
        }
    }

    bool isExploded = false;
    // 보드의 x를 숫자로 표시
    for (int row = 0; row<N; row++) {
        for (int col = 0; col<N; col++) {
            if (board[row][col] == 'x') {
                if (solution[row][col] == '*') {
                    isExploded = true;
                }
                else {
                    board[row][col] = '0';
                    for (int y = -1; y<=1; y++) {
                        for (int x = -1; x<=1; x++) {
                            if (row + y < 0 || row + y >= N || col + x < 0 || col + x >= N) {
                                continue;
                            }
                            if (solution[row+y][col+x] == '*') {
                                board[row][col] += 1;
                            }
                        }
                    }
                }
            }
        }
    }
    if (isExploded) {
        for (int i = 0; i<bombLocation.size(); i++) {
            board[get<0>(bombLocation[i])][get<1>(bombLocation[i])] = '*';
        }
    }

    for (int i = 0; i<N; i++) {
        for (int j = 0; j<N; j++) {
            cout<<board[i][j];
        }
        cout<<endl;
    }

    return 0;
}
