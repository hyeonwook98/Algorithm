#include<iostream>
using namespace std;
int hoje(int x, int y) {
	if (y == 0) return x;
	else return hoje(y,x%y);
}
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int j1, m2, m1,j2,rm,rj,a;
	cin >> j1 >> m1;
	cin >> j2 >> m2;
	rm = m1*m2; 
	j1 = j1*(rm / m1);
	j2 = j2*(rm / m2);
	rj = j1 + j2;
	a = hoje(rm, rj);
	rm = rm / a; rj = rj / a;
	cout << rj << ' ' << rm;
}
