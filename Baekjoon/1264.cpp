#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	string s;
	int count = 0;
	getline(cin, s);
	while (s != "#") {
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == 'a' || s[i] == 'A')
				count++;
			if (s[i] == 'e' || s[i] == 'E')
				count++;
			if (s[i] == 'i' || s[i] == 'I')
				count++;
			if (s[i] == 'o' || s[i] == 'O')
				count++;
			if (s[i] == 'u' || s[i] == 'U')
				count++;
		}
		cout << count << endl;
		count = 0;
		getline(cin, s);
	}
}
