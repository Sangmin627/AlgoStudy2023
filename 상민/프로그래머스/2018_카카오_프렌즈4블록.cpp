#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main() {
    std::cout << "Hello, World!" << std::endl;

    vector<string> board;
    int m = 4;
    int n = 5;

    bool needLoop = true;

    while (needLoop) {
        needLoop = false;
        vector<pair<int, int>> targetBlocks;
        for (int i = 0; i<m - 1; i++) {
            for (int j = 0; j<n - 1; j++) {
                bool isFilledSame = true;
                char tmp = board[i][j];
                if (tmp == '.') {
                    isFilledSame = false;
                    break;
                }

                for (int y = 0; y<2; y++) {
                    for (int x = 0; x<2; x++) {
                        if (x == 0 && y == 0) {
                            continue;
                        }
                        if (board[i+y][j+x] != tmp) {
                            isFilledSame = false;
                            break;
                        }
                    }
                    if (!isFilledSame) {
                        break;
                    }
                }
                if (isFilledSame) {
                    targetBlocks.push_back(make_pair(i,j));
                    needLoop = true;
                }
            }
        }

        for (int i = 0; i<targetBlocks.size(); i++) {
            int targetY = targetBlocks[i].first;
            int targetX = targetBlocks[i].second;

            for (int y = 0; y<2; y++) {
                for (int x = 0; x < 2; x++) {
                    board[targetY + y][targetX + x] = '.';
                }
            }
        }

        // 다 지운 상태임.
        for (int i = 0; i<n ; i++) { //가로행 우선
            for (int j = m-1; j>=0; j--) {
                int k = j;
                while(k < m && board[k][i] != '.' && board[k + 1][i] == '.') {
                    board[k+1][i] = board[k][i];
                    board[k][i] = '.';
                    k += 1;
                }
            }
        }
    }
    int answer = 0;
    for (int i = 0; i<m; i++) {
        for (int j = 0; j<n; j++) {
            if (board[i][j] == '.') {
                answer += 1;
            }
        }
    }

    return 0;
}
