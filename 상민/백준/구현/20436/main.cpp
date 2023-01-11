#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
int main() {

    map<char, tuple<int, int>> board;

    board['q'] = make_tuple(0,0);
    board['w'] = make_tuple(0,1);
    board['e'] = make_tuple(0,2);
    board['r'] = make_tuple(0,3);
    board['t'] = make_tuple(0,4);
    board['y'] = make_tuple(0,5);
    board['u'] = make_tuple(0,6);
    board['i'] = make_tuple(0,7);
    board['o'] = make_tuple(0,8);
    board['p'] = make_tuple(0,9);

    board['a'] = make_tuple(1,0);
    board['s'] = make_tuple(1,1);
    board['d'] = make_tuple(1,2);
    board['f'] = make_tuple(1,3);
    board['g'] = make_tuple(1,4);
    board['h'] = make_tuple(1,5);
    board['j'] = make_tuple(1,6);
    board['k'] = make_tuple(1,7);
    board['l'] = make_tuple(1,8);

    board['z'] = make_tuple(2,0);
    board['x'] = make_tuple(2,1);
    board['c'] = make_tuple(2,2);
    board['v'] = make_tuple(2,3);
    board['b'] = make_tuple(2,4);
    board['n'] = make_tuple(2,5);
    board['m'] = make_tuple(2,6);

    int vowelIndex[3] = {5, 5, 4};

    int leftY, leftX;
    int rightY, rightX;

    char initLeftChar, initRightChar; cin>>initLeftChar>>initRightChar;

    string word; cin>>word;

    leftY = get<0>(board[initLeftChar]);
    leftX = get<1>(board[initLeftChar]);

    rightY = get<0>(board[initRightChar]);
    rightX = get<1>(board[initRightChar]);

    int totalTime = 0;

    for (int i = 0; i<word.size(); i++) {
        char targetY = get<0>(board[word[i]]);
        char targetX = get<1>(board[word[i]]);

        // 이동하는 시간
        if (vowelIndex[targetY] <= targetX) { // 오른손으로 찍어야함
            totalTime += (abs(rightY - targetY) + abs(rightX - targetX));
            rightY = targetY;
            rightX = targetX;
        }
        else { // 왼손으로 찍어야함
            totalTime += (abs(leftY - targetY) + abs(leftX - targetX));
            leftY = targetY;
            leftX = targetX;
        }

        totalTime += 1;

    }
    cout<<totalTime;
    return 0;
}
