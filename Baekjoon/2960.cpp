#include<iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n, k,result;
	int p;
	int count = 0;
	int a[1001];
	cin >> n >> k;
	for (int i = 2; i <= n; i++) {
		a[i] = i;
	}
	for (int i = 2; i <= n; i++) {
		if (a[i] == 0)
			continue;
		if (count == k)
			break;
		for (int j = i; j <= n; j = j + i) {
			if (count == k) {
				break;
			}
			if (a[j] == 0)
				continue;
			p = a[j];
			a[j] = 0;
			count++;
		}
	}
	cout << p;
}
