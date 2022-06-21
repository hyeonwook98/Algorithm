#include<iostream>
#include<algorithm>
#include<string>
#include<stack>
using namespace std;
int main(void) {
	
	while (1) {
		string m;
		getline(cin, m);
		stack<char>s;
		int t = 1;
		//.이면 종료
		if(m.length() == 1 && m[0] == '.')
			break;
		//스택에 넣기
		for (int i = 0; i < m.length(); i++) {
			if (m[i] == '(' || m[i] == '[') {
				s.push(m[i]);
			}
			else if (m[i] == ')') {
				if (!s.empty() && s.top() == '(') {
					s.pop();
				}
				else {
					t = 0;
					break;
				}
					
			}
			else if (m[i] == ']') {
				if (!s.empty() && s.top() == '[') {
					s.pop();
				}
				else {
					t = 0;
					break;
				}
			}
		}
		if((s.empty())&&(t==1))
			cout << "yes" << endl;
		else 
			cout << "no" << endl;
		
	}
	return 0;
}
