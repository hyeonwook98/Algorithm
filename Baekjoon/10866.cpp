#include<cstring>
#include<cstdio>
int main(){
	int deque[10000];
	int size = 0;
	int t,n;
	char str[11];
	char s[8][11] = {"push_front","push_back","pop_front","pop_back",
			"size","empty","front","back"};
	scanf("%d",&t);
	while(t--){
		scanf(" %s",str);
		int i = 0;
		if(!strcmp(str,s[i++])){
			for(int i = size;i;--i){
				deque[i] = deque[i-1];
			}
			scanf("%d",&deque[0]);
			size++;
		}
		else if(!strcmp(str,s[i++])){
			scanf("%d",&deque[size]);
			size++;
		}
		else if(!strcmp(str,s[i++])){
			if(size == 0)
				printf("-1\n");
			else{
				printf("%d\n",deque[0]);
				for(int i =0;i<size;++i){
					deque[i] = deque[i+1];
				}
				size--;
			}
		}
		else if(!strcmp(str,s[i++])){
			if(size == 0)
				printf("-1\n");
			else{
				printf("%d\n",deque[--size]);
			}
		}
		else if(!strcmp(str,s[i++])){
			printf("%d\n",size);
		}
		else if(!strcmp(str,s[i++])){
			printf("%d\n",size ? 0 : 1);
		}
		else if(!strcmp(str,s[i++])){
			if(size == 0)
				printf("-1\n");
			else{
				printf("%d\n",deque[0]);
			}
		}
		else if(!strcmp(str,s[i++])){
			if(size == 0)
				printf("-1\n");
			else{
				printf("%d\n",deque[size-1]);
			}
		}
	}
}
