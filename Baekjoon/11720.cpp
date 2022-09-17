#include <iostream>
int main() {

	int n;
	char number;
	int sum = 0;
	std::cin >> n;
	for (int i = 0; i < n; i++) {
		std::cin >> number;
		sum += number - 48;
	}
	std::cout << sum;
	return 0;
}
