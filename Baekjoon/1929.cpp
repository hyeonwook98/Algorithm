#include<iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int m, n;
	cin >> m;
	cin >> n;
	int *a = new int[n+1];
	for (int i = 2; i <= n; i++) {
		a[i] = i;
	}
	for (int i = 2; i <= n; i++) {
		for (int j = i*2; j <= n; j += i) {
			a[j] = 0; 
		}
	}
	for (int i = m; i <= n; i++) {
		if (a[i] != 0)
			cout << a[i]<<'\n';
	}
	delete[] a;
	
}
