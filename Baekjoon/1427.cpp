#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
bool desc(char a, char b) {
	return a > b;
}
char arr[10];
int main(void) {

	cin >> arr;

	sort(arr, arr + strlen(arr), desc);
	for (int i = 0; i<strlen(arr); i++) {
		cout << arr[i];
	}

	return 0;
}
