#include<iostream>
#include<queue>
#include<functional>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
	int n, x;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x;
		if (x == 0) {
			if (q.empty())
				cout << 0 << '\n';
			else {
				cout << q.top().second << '\n';
				q.pop();
			}
		}
		else {
			q.push(make_pair(abs(x),x));
		}
	}
}
