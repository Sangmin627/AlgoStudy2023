#include <iostream>
#include <string.h>
using namespace std;

int power[11][11];
int visited[11];

int maxTotalPower = 0;

void dfs(int idx) {
    if (idx == 11) {
        int totalPower = 0;
        for (int i = 0; i<11; i++) {
            totalPower += visited[i];
        }
        maxTotalPower = (maxTotalPower < totalPower) ? totalPower : maxTotalPower;
        return;
    }

    for (int i = 0; i<11; i++) {
        if (power[idx][i] != 0 && visited[i] == 0) {
            visited[i] = power[idx][i];
            dfs(idx+1);
            visited[i] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int T;
    cin>>T;

    for (int i = 0; i<T; i++) {
        maxTotalPower = 0;
        for (int j = 0; j<11; j++) {
            for (int k = 0; k<11; k++) {
                cin>>power[j][k];
            }
        }

        dfs(0);
        cout<<maxTotalPower<<"\n";
    }

    return 0;
}
