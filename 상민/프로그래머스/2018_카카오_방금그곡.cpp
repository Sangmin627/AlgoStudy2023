#include <iostream>
#include <sstream>

using namespace std;

struct CastInfo {
    int playTime;
    string title;
    vector<string> code;
};

int timeFrom(string str) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, ':')) {
        result.push_back(buffer);
    }
    int hour = stoi(result[0]);
    int min = stoi(result[1]);

    return hour * 60 + min;
}

int playTimeFrom(string from, string to) {
    return timeFrom(to) - timeFrom(from);
}

vector<string> codeFrom(string musicCode) {
    vector<string> ret;
    for (int i = 0; i<musicCode.size(); i++) {
        if (i != musicCode.size() - 1 && musicCode[i+1] == '#') {
            ret.push_back(musicCode.substr(i, 2));
            i++;
        } else {
            ret.push_back(musicCode.substr(i, 1));
        }
    }
    return ret;
}

CastInfo translate(string str) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, ',')) {
        result.push_back(buffer);
    }
    CastInfo info;
    info.playTime = playTimeFrom(result[0], result[1]);
    info.title = result[2];
    info.code = codeFrom(result[3]);
    return info;
}

bool checkMusic(vector<string> musicCode, vector<string> m) {
    for (int i = 0; i<musicCode.size(); i++) {
        int idx = 0;
        for (int j = i; j<musicCode.size(); j++) {
            if (musicCode[j] == m[idx]) {
                idx += 1;
            } else {
                break;
            }
            if (idx == m.size()) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<string> musicinfos = {"03:00,03:30,FOO,CC#B", "12:00,12:10,HIHIHI,CDCDCDE"};
    string m = "CDCDE";
    vector<string> mVec = codeFrom(m);
    CastInfo musicInfo;
    musicInfo.title = "(None)";
    musicInfo.playTime = 0;

    for (int i = 0; i<musicinfos.size(); i++) {
        CastInfo info = translate(musicinfos[i]);

        vector<string> fullCode;
        for (int j = 0; j<info.playTime; j++) {
            fullCode.push_back(info.code[j%info.code.size()]);
        }

        if (checkMusic(fullCode, mVec)) {
            if (info.playTime > musicInfo.playTime) {
                musicInfo = info;
            }
        }
    }

    cout<<musicInfo.title;
    return 0;
}

