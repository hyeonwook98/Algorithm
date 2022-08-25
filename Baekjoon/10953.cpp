#include <iostream>
#include <string>
int main() {
	using namespace std;
	int tc;
	int a, b;
	string s;
	cin >> tc;
	for (int i = 0; i < tc; i++) {
		cin >> s;
		for (int j = 0; j < s.length(); j++) {
			if (s[j] == ',') {
				a = s[j - 1]-'0';
				b = s[j + 1]-'0';
			}
		}
		cout << a+b << endl;
	}
}
