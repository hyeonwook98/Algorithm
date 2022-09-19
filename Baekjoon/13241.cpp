#include<iostream>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	long long f,s,tmp,max,min;
		cin >> f >> s;
		if (f > s) {
			max = f; min = s;
			while (1) {
				if (f%s == 0)
					break;
				tmp = f%s; f = s; s = tmp;
			}
			cout << (max*min) / s<<endl;
		}
		else {
			max = s; min = f;
			while (1) {
				if (s%f == 0)
					break;
				tmp = s%f; s = f; f = tmp;
			}
			cout << (max*min) / f<<endl;
		}
}
