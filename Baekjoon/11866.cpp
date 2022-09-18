#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	queue<int>q1;
	int n, k;
	cin >> n; 
	cin >> k;
	for (int i = 1; i <= n; i++) {
		q1.push(i);
	}
	cout << '<';
	while (1) {
		for (int i = 0; i < k-1; i++) {
			q1.push(q1.front());
			q1.pop();
		}
		cout<<q1.front();
		q1.pop();
		if (q1.empty())
			break;
		cout << ", ";
	}
	cout << '>';
}
