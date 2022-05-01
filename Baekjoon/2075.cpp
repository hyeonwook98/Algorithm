#include<iostream>
#include<queue>
#include<functional>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	priority_queue<int,vector<int>,greater<int>> pq;
	int n,number;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> number;
		pq.push(number);
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> number;
			pq.push(number);
		}
		for (int j = 0; j < n; j++) {
			pq.pop();
		}
	}
	cout << pq.top();
}
