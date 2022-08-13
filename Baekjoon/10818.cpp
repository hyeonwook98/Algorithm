#include <iostream>
int main() {
	using namespace std;
	int n;
	int a;
	cin >> n;
	cin >> a;
	int min = a , max = a;
	for (int i = 0; i < n-1; i++) {
		
		cin >> a;
		if (min > a)
			min = a;
		else if(max<a)
			max = a;
	}
	cout << min <<" " <<max;
	
	
}
