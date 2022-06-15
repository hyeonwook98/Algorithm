#include<iostream>
#include<algorithm>
#include<string>
#include<stack>
using namespace std;
int main(void) {
	int count = 0;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string str;
		stack<char>s;
		cin >> str;
		for (int j = 0; j < str.length(); j++) {
			if (!s.empty() && s.top() == str[j]) {
				s.pop();
			}
			else
				s.push(str[j]);
		}
		if (s.empty())
			count++;
	}
	cout << count << endl;
	return 0;
}
