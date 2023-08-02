#include <iostream>
#include <string.h>
using namespace std;

int N, M;
bool nemo[26][26];
int totalCnt = 0;

void dfs(int y, int x) {
    if (y == N) {
        totalCnt++;
        return;
    }
    int up = 0, left = 0, leftUp = 0;
    if (y-1 >= 0) {
        up = nemo[y-1][x];
    }
    if (x - 1 >= 0) {
        left = nemo[y][x-1];
    }
    if (y - 1 >= 0 && x - 1 >= 0) {
        leftUp = nemo[y-1][x-1];
    }

    int newY = (x+1 == M) ? y+1 : y;
    int newX = (x+1 == M) ? 0 : x+1;


    // 전부 1이면? 무조건 0
    if (up == 1 && left == 1 && leftUp == 1){
        nemo[y][x] = 0;
        dfs(newY, newX);
    } else { //안채워지거나 낭떨어지
        nemo[y][x] = 0;
        dfs(newY, newX);
        nemo[y][x] = 1;
        dfs(newY, newX);
    }
}

int main() {

    cin>>N>>M;
    for (int i = 0; i<26; i++) {
        memset(nemo[i], 0, sizeof(nemo[i]));
    }

    dfs(0, 0);
    cout<<totalCnt;

    return 0;
}
