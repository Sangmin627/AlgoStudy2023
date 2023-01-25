#include <iostream>
using namespace std;

string func1(int len) {

    int aCount = len/4;
    int bCount = (len - aCount*4)/2;

    string ret = "";
    for (int i = 0; i<aCount; i++) {
        ret += "AAAA";
    }
    for (int i = 0; i<bCount; i++) {
        ret += "BB";
    }
    return ret;
}

int main() {

    string s; cin>>s;

    int counter = 0;

    string ret = "";

    for (int i = 0; i<s.size(); i++) {
        if (s[i] == 'X') {
            counter ++;
        } else {
            if (counter != 0) {
                if (counter % 2 != 0) {
                    cout<<-1;
                    return 0;
                }
                ret += func1(counter);

                counter = 0;
            }
            ret += ".";
        }
    }
    if (counter != 0) {
        if (counter % 2 != 0) {
            cout<<-1;
            return 0;
        }
        ret += func1(counter);
    }

    cout<<ret;

    return 0;
}
