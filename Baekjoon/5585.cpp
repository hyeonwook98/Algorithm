#include<iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int money;
	int count = 0;
	int result;
	cin >> money;
	result = 1000 - money;
	while (result != 0) {
		if (result >= 500) {
			result -= 500;
			count++;
		}
		else if (result >= 100) {
			result -= 100;
			count++;
		}
		else if (result >= 50) {
			result -= 50;
			count++;
		}
		else if (result >= 10) {
			result -= 10;
			count++;
		}
		else if (result >= 5) {
			result -= 5;
			count++;
		}
		else if (result >= 1) {
			result -= 1;
			count++;
		}
	}
	cout << count;
}
