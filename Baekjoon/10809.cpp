#include <iostream>
#include <string>
int main() {
	using namespace std;
	int count = 0;
	string s;
	cin >> s;
	int a[26];
	for (int i = 0; i < 26; i++) {
		a[i] = -1;
	}
	for (int i = 0; i < s.length(); i++) {
		if(a[s[i] - 97]<0)
		a[s[i]-97] = count;
			count++;
	}
	for (int i = 0; i < 26; i++) {
		cout<<a[i]<<" ";
	}
}
