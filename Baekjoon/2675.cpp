#include <iostream>
#include <string>
int main() {
	using namespace std;
	int number, count;
	string s="";
	cin >> number;
	for (int i = 0; i < number; i++) {
		cin >> count >> s;
		for (int j = 0; j < s.length(); j++) {
			for (int k = 0; k < count; k++) {
				cout << s[j];
			}
		}
		cout << endl;
	}
	return 0;
}
