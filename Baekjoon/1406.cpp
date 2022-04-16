#include<iostream>
#include<algorithm>
#include<string>
#include<stack>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int number;
	string alr,a;
	stack<char>s;
	stack<char>r;
	cin >> alr;
	cin >> number;
	for (int i = 0; i < alr.length(); i++) {
		s.push(alr[i]);
	}
	cin.ignore();
	for (int i = 0; i < number; i++) {
		getline(cin, a);
		if (a == "L") {
			if (!s.empty()) {
				r.push(s.top());
				s.pop();
			}
		}
		else if (a == "D") {
			if (!r.empty()) {
				s.push(r.top());
				r.pop();
			}
		}
		else if (a == "B") {
			if (!s.empty()) {
				s.pop();
			}
		}
		else if (a[0] == 'P'&&a.length() == 3) {
			s.push(a[2]);
		}
	}
	for (int i = 0; !s.empty(); i++) {
		r.push(s.top());
		s.pop();
	}
	for (int i = 0; !r.empty(); i++) {
		cout << r.top();
		r.pop();
	}
	return 0;
}
