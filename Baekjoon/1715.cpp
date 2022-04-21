#include<iostream>
#include<queue>
#include<functional>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	priority_queue<int, vector<int>, greater<int>> pq;
	int n, number, f, s;
	int sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> number;
		pq.push(number);
	}
	while (pq.size() != 1) {
		f = pq.top();
		pq.pop();
		s = pq.top();
		pq.pop();
		pq.push(f + s); sum += (f + s);
	}
	cout << sum << endl;
}
