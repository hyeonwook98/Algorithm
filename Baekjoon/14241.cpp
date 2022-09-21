#include<iostream>
#include<queue>
#include<functional>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0); 
	int n, s,first,second;
	int sum = 0;
	cin >> n;
	priority_queue<int> pq;
	for (int i = 0; i < n; i++) {
		cin >> s;
		pq.push(s);
	}
	for (int i = 0; i < n - 1; i++) {
		first = pq.top();
	    pq.pop();
		second = pq.top();
		pq.pop();
		pq.push(first+second);
		sum = sum+(first*second);
		first = 0;  second = 0;
	}
	cout << sum << endl;
}
