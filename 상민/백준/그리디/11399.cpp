#include <iostream>
#include <algorithm>
using namespace std;

int main() {

    int N; cin>>N;
    int time[N];

    for (int i = 0; i<N; i++) {
        cin>>time[i];
    }
    sort(time, time+N);
    int totalTime = 0;
    int timeSum = 0;

    for (int i = 0; i<N; i++) {
        totalTime += time[i];
        timeSum += totalTime;
    }

    cout<<timeSum;

    return 0;
}