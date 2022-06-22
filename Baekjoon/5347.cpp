#include<iostream>
using namespace std;
long long hoje(int x, int y) {
	if (y == 0) return x;
	else return hoje(y,x%y);
}
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	long long n, a, b;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		cout << (a*b)/hoje(a, b)<<endl;
	}
}
