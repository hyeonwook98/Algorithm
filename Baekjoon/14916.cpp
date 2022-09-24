#include<iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n;
	int count = 0;
	cin >> n;
	if (n == 1 || n == 3) {
		count = -1;
	}
	else {
		if (n % 5 == 1 || n % 5 == 3) {
			count += n / 5 - 1;  n = n - (n / 5 - 1) * 5;
		}
		else {
			count += n / 5; n = n % 5;
		}
		count += n / 2;
	}
	cout << count;
}
