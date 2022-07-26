#include<iostream>
#include<algorithm>
#include<cstring>
#include<stack>
using namespace std;
int main(void) {
	stack<int>s;
	int n, num;
	int sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (num == 0) {
			s.pop();
		}
		else
			s.push(num);
	}
	for (int i = 0; !s.empty(); i++) {
		sum += s.top();
		s.pop();
	}
	cout << sum << endl;
	return 0;
}
