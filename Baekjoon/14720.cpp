#include<iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n,number,s;
	int count = 0;
	cin >> n;
	int a[1000];
	for (int i = 0; i < n; i++) {
		cin >> number;
		a[i] = number;
	}
	for (int i = 0; i < n; i++) {
		if (a[i] == 0) {
			number = i;  count++; s = a[i]; break;
		}
	}
	for (int i = number+1; i < n; i++) {
		if (s == 0 && a[i] == 1) {
			count++; s = a[i];
		}
		else if (s == 1 && a[i] == 2) {
			count++; s = a[i];
		}
		else if (s == 2 && a[i] == 0) {
			count++; s = a[i];
		}
	}
	cout << count;
}
