#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
int main(void) {
    // 自分の得意な言語で
    // Let's チャレンジ！！
    string str, s;
    vector<string> v;
    getline(cin, str);
    stringstream ss{str};

    while (getline(ss, s, ',')) {
        v.push_back(s);
    }
    for (const string& s : v) {
        cout << s << endl;
    }

    return 0;
}