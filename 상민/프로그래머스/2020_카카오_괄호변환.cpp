#include <iostream>
#include <string>
using namespace std;

bool isCorrectString(string s) {
    int isRightCounter = 0;
    for (int i = 0; i<s.size(); i++) {
        if (s[i] == '(') {
            isRightCounter -= 1;
        } else {
            isRightCounter += 1;
        }

        if (isRightCounter > 0) {
            return false;
        }
    }
    return true;
}

string dnq(string s) {
    if (s.empty()) {
        return s;
    }
    int balanceCount = 0;
    string u = "";
    string v = "";
    for (int i = 0; i<s.size(); i++) {
        if (s[i] == '(') {
            balanceCount -= 1;
        } else {
            balanceCount += 1;
        }

        if (balanceCount == 0) {
            u = s.substr(0, i+1);
            v = s.substr(i+1, s.size() - (i + 1));
            break;
        }
    }

    if (isCorrectString(u)) {
        return u + dnq(v);
    } else {
        string tmp = "(";
        tmp += dnq(v);
        tmp += ")";
        u.erase(u.begin());
        u.erase(u.end() - 1);
        string newU;
        for (int i = 0; i<u.size(); i++) {
            if (u[i] == '(') {
                newU += ')';
            } else {
                newU += '(';
            }
        }
        tmp += newU;
        return tmp;
    }
}

int main() {
    string s = "()))((()";
    cout<<dnq(s);

    return 0;
}


