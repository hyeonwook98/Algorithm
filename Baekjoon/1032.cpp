#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int number;
	string s, result;
	cin >> number;
	cin >> s;
	result = s;
	for (int i = 0; i < number-1; i++) {
		cin >> s;
		for (int j = 0; j < s.length(); j++) {
			if (result[j] != s[j]) {
				result[j] = '?';
			}
		}
	}
	cout << result;
}
