import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int s[] = new int[10001];
		for(int i=0;i<10000;i++) {
			
			if(math(i)<=10000)
					s[math(i)]=1;
		}
		for(int i=0;i<10000;i++) {
			if(s[i]==0) {
				System.out.println(i);
			}
		}
	}
	static int math(int x) {
		int sum=0;
		sum=x+(x/1000)+(x%1000/100)+(x%1000%100/10)+(x%10);
		return sum;
	}
}
