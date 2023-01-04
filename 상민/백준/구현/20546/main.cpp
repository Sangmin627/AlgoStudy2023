#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int initMoney; int JoonMoney; int SungMoney;
    int JoonCount = 0; int SungCount = 0;

    cin>>initMoney;

    JoonMoney = initMoney;
    SungMoney = initMoney;

    int befJooga = -1;
    int state = 0; // -1, 0, 1
    int stateCounter = 0;

    for (int i = 0; i<14; i++) {
        int jooga; cin>>jooga;

        // Joon
        int JoonCurCount = JoonMoney / jooga;
        JoonMoney -= JoonCurCount * jooga;
        JoonCount += JoonCurCount;

        // Sung
        if (i != 0) {
            int newState = jooga - befJooga;

            newState = (newState == 0) ? 0 : newState / abs(newState);
            stateCounter = (newState == state) ? (stateCounter + 1) : 1;
            state = newState;

            if (stateCounter >= 3) {
                if (state == -1) {
                    int SungCurCount = SungMoney / jooga;
                    SungMoney -= SungCurCount * jooga;
                    SungCount += SungCurCount;
                }
                else if (state == 1){
                    SungMoney += SungCount * jooga;
                    SungCount = 0;
                }
            }
        }
        befJooga = jooga;
    }

    int JoonTotal = JoonMoney + JoonCount * befJooga;
    int SungTotal = SungMoney + SungCount * befJooga;

    if (JoonTotal > SungTotal) {
        cout<<"BNP";
    } else if (JoonTotal == SungTotal) {
        cout<<"SAMESAME";

    } else {
        cout<<"TIMING";
    }

    return 0;
}
