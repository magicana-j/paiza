// 標準入力から配列データを読み込もう
#include <stdio.h>

int main(void) {
    char buf[100];
    int n;
    fgets(buf, sizeof(buf), stdin);
    sscanf(buf, "%d", &n);

    int data[20];
    for (int i = 0; i < n; i++) {
        int x;
        fgets(buf, sizeof(buf), stdin);
        sscanf(buf, "%d", &x);

        // ここで配列 data に順番に x 変数の値を代入する
        data[i] = x;
    }

    for (int i = 0; i < n; i++) {
        printf("data[%d] : %d\n", i, data[i]);
    }
}
