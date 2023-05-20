#include <iostream>
#include <istream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(void) {
    int n;
    cin >> n;

    string str;
    getline(cin, str);
    stringstream ss{str};

    vector<string> v;
    string buf;
    while (getline(ss, buf, ' ')) {
        v.push_back(buf);
    }

    return 0;
}