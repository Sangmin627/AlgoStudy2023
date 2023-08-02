#include <iostream>
#include <string.h>
#include <limits.h>
using namespace std;
int main() {
    int N;
    int board[100001];

    int sum[100001];
    memset(board, 0, sizeof(board));
    cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);
    cin>>N;

    cin>>board[0];
    sum[0] = board[0];
    for (int i = 1; i<N; i++) {
        cin>>board[i];
        sum[i] = sum[i-1] + board[i];
    }

    // 이분탐색으로 꿀통 위치를 정하고, 좌우 혹은 좌좌, 우우에서 정하기..?

    // 벌벌통, 벌통벌, 통벌벌

    // 벌벌통
    int bulbulTongSum = sum[N-1] - board[0];
    int bulbulTongMax = INT_MIN;

    // 벌통벌
    int bulTongBulSum = 0;
    int bulTongBulMax = INT_MIN;

    int tongBulbulSum = sum[N-1] - board[N-1];
    int tongBulbulMax = INT_MIN;


    for (int i = 1; i<N-1; i++) {
        bulbulTongMax = max(bulbulTongMax, sum[N-1]-sum[i] - board[i]); //벌의 위치

        bulTongBulMax = max(bulTongBulMax, sum[i] - board[0] + sum[N-1]-sum[i-1] - board[N-1]); //통의 위치

        tongBulbulMax = max(tongBulbulMax, sum[i-1] - board[i]); //벌의 위치
    }

    bulbulTongSum += bulbulTongMax;

    bulTongBulSum += bulTongBulMax;

    tongBulbulSum += tongBulbulMax;

    int ret = max(bulbulTongSum, max(bulTongBulSum, tongBulbulSum));

    cout<<ret;

    return 0;
}
