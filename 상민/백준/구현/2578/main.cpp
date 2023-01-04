#include <iostream>
using namespace std;
int main() {

    int board[5][5];

    for (int row = 0; row<5; row++) {
        for (int col = 0; col<5; col++) {
            cin>>board[row][col];
        }
    }

    int horizontal[5];
    int vertical[5];
    int leftHeadedDiagonal = 5;
    int rightHeadedDiagonal = 5;
    for (int i = 0; i<5; i++) {
        horizontal[i] = 5;
        vertical[i] = 5;
    }

    int lineCount = 0;
    for (int i = 0; i<25; i++) {
        int num; cin>>num;
        for (int row = 0; row < 5; row++) {
            for (int col = 0; col<5; col++) {
                if (board[row][col] == num) {
                    lineCount = ((horizontal[row] -= 1) == 0) ? (lineCount + 1) : lineCount;
                    lineCount = ((vertical[col] -= 1) == 0) ? (lineCount + 1) : lineCount;
                    if (row == col) {
                        lineCount = ((leftHeadedDiagonal -= 1) == 0) ? (lineCount + 1) : lineCount;
                    }
                    if (row + col == 4) {
                        lineCount = ((rightHeadedDiagonal -= 1) == 0) ? (lineCount + 1) : lineCount;
                    }

                    if (lineCount >= 3) {
                        cout<<i+1;
                        return 0;
                    }
                }
            }
        }
    }


    return 0;
}
