#include <stdio.h>
#include <limits.h>

int N, K;
int words[51];

int maxWordCount = INT_MIN;

void dfs(int i, int depth, int saved) { // i = char - 'a'
    if (depth == K) { //여기서 총 단어수를 알아야함..!
        int wordCount = 0;
        for (int j = 0; j<N; j++) { //단어들에 i알파벳이 포함되는지 여부
            if ((saved & words[j]) == words[j]) { //포함된다면???
                wordCount++;
            }
        }
        maxWordCount = (maxWordCount < wordCount) ? wordCount : maxWordCount;
    }

    for (int j = i+1; j<='z'-'a'; j++) { //싹다 돌면서 추가된 단어를 유지한다.
        dfs(j, depth+1, saved | (1<<j));
    }
}

int main() {
    // 일단 K가 5이상 이여야 뭐든 읽을 수 있음. 5아래면 바로 거르자

    // 단어입력받고, 그거를 dfs로 타고들어가자!
    scanf("%d %d\n", &N, &K);
    if (K < 5) {
        printf("%d", 0);
        return 0;
    }

    K -= 5;

    for (int i = 0; i<N; i++) { //못읽는 문자를 여기서도 걸러야하나?
        int mask = 0;
        while (1) {
            char c;
            scanf("%c", &c);

            if (c == '\n') { break; }
            else if (c == 'a' || c == 'n' || c == 't' || c == 'c' || c == 'i') { continue; }
            c -= 'a';
            mask |= (1<<c);
        }

        words[i] = mask;
    }

    dfs(-1, 0, 0);


    printf("%d", maxWordCount);


    return 0;
}
