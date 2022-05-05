#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
using namespace std;
int main(void) {
	queue<int>q;
	int n;
	int a;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	for (int i = 2; 1<q.size(); i++) {
		if ((i % 2) == 0) {
			q.pop();
		}
		else {
			q.push(q.front());
			q.pop();
		}
	}
	cout << q.front();
}
