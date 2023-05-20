#include <iostream>
#include <string>
using namespace std;
int main(void) {
    // 自分の得意な言語で
    // Let's チャレンジ！！
    int n;
    cin >> n;
    string dummy;
    getline(cin, dummy);

    string str;
    for (int i = 0; i < n - 1; i++) {
        getline(cin, str, ',');
        cout << str << endl;
    }
    getline(cin, str);
    cout << str << endl;
    return 0;
}