#include<iostream>
#include<queue>
#include<functional>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n,p;
	int sum = 0, sum2 = 0;
	cin >> n;
	priority_queue<int,vector<int>,greater<int>> pq;
	for (int i = 0; i < n; i++) {
		cin >> p; pq.push(p);
	}
	for (int i = 0; i < n; i++) {
		sum += pq.top(); sum2 += sum; pq.pop();
	}
	cout << sum2;
}
