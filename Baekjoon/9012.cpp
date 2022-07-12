#include<iostream>
#include<algorithm>
#include<string>
#include<stack>
using namespace std;
int main(void) {
	int a;
	char inp[51];
	cin >> a;
	while (a--) {
		int t = 0;
		cin >> inp;
		for (int i = 0; inp[i]; i++) {
			if (inp[i] == '(')
				t++;
			else
				t--;
			if (t < 0)
				break;
		}
		if (t == 0)
			cout << "YES" << endl;
		else 
			cout << "NO" << endl;
	}
}
