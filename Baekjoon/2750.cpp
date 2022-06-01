#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int n;
	scanf("%d", &n);
	int s[1000];
	for (int i = 0; i < n; i++) {
		scanf("%d", &s[i]);
	}
	sort(s, s + n);
	for (int i = 0; i < n; i++) {
		printf("%d\n", s[i]);
	}
}
