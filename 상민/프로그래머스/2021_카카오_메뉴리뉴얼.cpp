#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

unordered_map<string, int> dict;
vector<string> orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
void dfs(string &v, string s, int n) {
    dict[s] += 1;
    for (int i = n+1; i<v.size(); i++) {
        dfs(v, s+v[i], i);
    }
}

int main() {
    std::cout << "Hello, World!" << std::endl;

    vector<int> course = {2,3,4};

    for (int i = 0; i<orders.size(); i++) {
        string order = orders[i];
        sort(order.begin(), order.end());
        dfs(order, "", -1);
    }

    vector<string> menuList;
    int maxCounter[11]; //maxCounter[음식수] = 최대주문수
    memset(maxCounter, 0, 11 * sizeof(int));

    for(auto elem : dict){
        if (elem.second >= 2 && find(course.begin(), course.end(), elem.first.size()) != course.end()) {
            if (maxCounter[elem.first.size()] < elem.second) {
                maxCounter[elem.first.size()] = elem.second;
            }
        }
    }

    for (auto elem : dict) {
        // elem.second엔 0이 절대 없음.
        if (elem.second == maxCounter[elem.first.size()]) {
            menuList.push_back(elem.first);
        }
    }

    sort(menuList.begin(), menuList.end());

    for (int i = 0; i<menuList.size(); i++) {
        cout<<menuList[i]<<" ";
    }
    return 0;
}
