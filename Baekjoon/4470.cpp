#include <iostream>
#include <string>
int main() {
	using namespace std;
	int n;
	string s;
	cin >> n;
	cin.ignore();
	for (int i = 0; i < n; i++) {
		getline(cin, s);
		cout << i+1 << ". " << s<<endl;
	}
}
