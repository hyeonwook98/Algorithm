#include <iostream>
#include <string>
int main() {
	using namespace std;
	int n;
	int count = 0;
	int ac[26], bc[26];
	string a, b;
	
	cin >> n;
	cin.ignore();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 26; j++) {
			ac[j] = 0;
			bc[j] = 0;
		}
		cin >> a >> b;
		if (a.length() == b.length()) {
			for (int j = 0; j < a.length(); j++) {
				ac[a[j] - 97]++;
				bc[b[j] - 97]++;
			}
			while (count<26) {
				if (ac[count] != bc[count])
					break;
				count++;
			}
			if (count == 26) {
				cout << a << " & " << b << " are anagrams."<<endl;
			}
			else 
				cout << a << " & " << b << " are NOT anagrams." << endl;
		}
		else {
			cout << a << " & " << b << " are NOT anagrams." << endl;
		}
		count = 0;
	}
}
