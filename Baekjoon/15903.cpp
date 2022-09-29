#include<iostream>
#include<queue>
#include<functional>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	priority_queue<long long,vector<long long>,greater<long long>>pq; //최소힙
	int n, m, a;
	long long sum = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> a;
		pq.push(a);
	}
	for (int j = 0; j < m; j++) {
		for (int i = 0; i < 2; i++) {
			sum += pq.top();
			pq.pop();
		}
		pq.push(sum); pq.push(sum);
		sum = 0;
	}
	for (int i = 0; !pq.empty(); i++) {
		sum+=pq.top();
		pq.pop();
	}
	cout << sum<<endl;
}
