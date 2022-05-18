import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		
		int x=input.nextInt();
		int y=input.nextInt();
		int z=input.nextInt();
		int result=(x*y*z);
		int temp=result;
		int c=0;
		while(temp!=0) {
			c++;
			temp/=10;
		}
		int [] s = new int[c];
		int []s2 = new int[9];
		for(int i=1;i<=s.length;i++) {
			s[s.length-i]=result%10;
			result/=10;
			
		}                 //s배열에 잘들어감!!
		
		for(int j=0;j<=9;j++) {
			int count=0;
			for(int i=0;i<s.length;i++) {
			
			if(s[i]==j) {
				count++;
				}
			
		    }
			System.out.println(count);//s2[j]=count;
		}
		/*for(int i=0;i<s2.length;i++) {
			System.out.println(s2[i]);
		}*/
	}

}
