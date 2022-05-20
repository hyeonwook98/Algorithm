#include<iostream>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int a, b,c,min,max;
	cin >>a>>b;
	if (a == b) {
		cout << a << endl;
		cout << a << endl;
}
else if (a > b) {
		max = a; min = b;
		//최대공약수
		while (1) {
			if ((a%b) == 0) {
				break;
			}
			c = (a%b); a = b; b = c;
		}
		cout << b << endl;
		//최소공배수
		cout << (max*min)/b<<endl;
	}
	else {
		max = b; min = a;
		while (1) {
			if ((b%a) == 0) {
				break;
			}
			c = (b%a); b = a; a = c;
		}
		cout << a << endl;
		//최소공배수
		cout << (max*min) / a <<endl;
	}

}
