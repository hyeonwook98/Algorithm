#include<iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n, k, a; int count = 0; int dong[10];
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> a; dong[i] = a;
	}
	for (int i = n-1; i >= 0; i--) {
		count += (k / dong[i]); k = k%dong[i];
	}
	cout << count;
	return 0;
}
