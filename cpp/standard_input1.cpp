#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s);
    istringstream iss(s);
    string t;
    while (iss >> t) {
        cout << t << endl;
    }
    return 0;
}
