#include<iostream>
using namespace std;
void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b = temp;
}

int gcd(int a, int b) {
	int temp;
	if (a < b)
		swap(a, b);
	while (b != 0) {
		temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t, n,a,b;
	long long sum = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n;
		int num[100];
		for (int j = 0; j < n; j++) {
			int c;
			cin >> c; num[j] = c;
		}
		for (int j = 0; j < n-1; j++) {
			for (int z = j+1; z < n; z++) {
				sum += gcd(num[j], num[z]);
			}
		}
		cout << sum << endl;
		sum = 0;
	}
}
