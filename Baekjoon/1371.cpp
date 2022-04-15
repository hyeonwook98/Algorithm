#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	
	string s;
	int max = 0;
	int alr[26];
	for (int i = 0; i < 26; i++) {
		alr[i] = 0;
	}
	while (cin >> s)
	{

		for (int i = 0; i < s.length(); i++)

			if (s[i] >= 'a' && s[i] <= 'z')

				alr[s[i] - 'a']++;

		s.clear();

	}
	for (int i = 0; i < 26; i++) {
		if (max < alr[i]) {
			max = alr[i];
		}
	}
	for (int i = 0; i < 26; i++) {
		if (max == alr[i]) {
			cout << (char)(i + 97);
		}
	}
}
