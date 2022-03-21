#include<iostream>
#include<deque>
using namespace std;
int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	deque<int>d;
	int n, m,number;
	int count=0;
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		d.push_back(i);
	}
	for (int i = 0; i < m; i++) {
		cin >> number;
		if (number == d.front()) {
			d.pop_front();
		}
		else {
			int index = 1;
			//인덱스찾기
			for (int i = 0; i < d.size(); i++) {
				if (d[i] == number) {
					index = i;
					break;
				}
			}
			int left = index ;
			int right = d.size() - (index + 1);
			if (left > right) {
				for (int j = 0; j < right+1; j++) {
					d.push_front(d.back());
					d.pop_back();
					count++;
				}
				d.pop_front();
			}
			else {
				for (int j = 0; j < left; j++) {
					d.push_back(d.front());
					d.pop_front();
					count++;
				}
				d.pop_front();
			}
		}
	}
	cout << count<<endl;
	return 0;
}
