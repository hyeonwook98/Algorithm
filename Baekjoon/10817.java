import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int mid=0;
		int a=input.nextInt();
		int b=input.nextInt();
		int c=input.nextInt();
		
		if(a>=b&&a>=c) {
			if(b>=c)
				mid=b;
			else
				mid=c;
		}
		if(b>=a&&b>=c) {
			if(a>=c)
				mid=a;
			else 
				mid=c;
		}
		if(c>=a&&c>=b) {
			if(a>=b)
				mid=a;
			else
				mid=b;
		}
		System.out.println(mid);
	}

}
