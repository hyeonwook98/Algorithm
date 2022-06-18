#include <iostream>
#include <string>
int main() {
	using namespace std;
	int n;
	cin >> n;
	cin.ignore();
	string s;
	for (int i = 0; i < n; i++) {
		getline(cin, s);
		if (97 <= s[0] && s[0] <= 122) {
			s[0] = s[0] - 32;
		}
		cout << s<<endl;
	}
}
