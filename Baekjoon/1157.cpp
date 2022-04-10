#include <iostream>
#include <string>
int main() {
	using namespace std;
	int alr[26];
	int count = 0;
	int index = 0;
	int max;
	string s;
	cin >> s;
	//배열에 초기값 0 넣기
	for (int i = 0; i < 26; i++) {
		alr[i] = 0;
	}
	//알파벳에맞는 배열인덱스에 카운트
	for (int i = 0; i < s.length(); i++) {
		//소문자일때
		if (s[i] > 96 && s[i]<123) {
			alr[(s[i] - 97)]++;
		}
		//대문자일때
		if(s[i]>64 && s[i]<91) {
			alr[(s[i] - 65)]++;
		}
		else {

		}
	}
	max = alr[0];
	for (int i = 1; i < 26; i++) {
		if (max< alr[i])
			max = alr[i];
	}
	for (int i = 0; i < 26; i++) {
		if (max == alr[i]) {
			count++;
			index = i;
		}
	}
	if (count ==1)
		cout << (char)(index + 65);
	else
		cout << "?";
}
