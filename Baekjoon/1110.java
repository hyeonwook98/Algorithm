import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number,a;
		int result=100;
		int c=0;
		number=input.nextInt();
		a=number;
		while(number!=result) {
			int x,y,z;
			x=(a/10);
			y=(a%10);
			z=(x+y)%10;
			result=(y*10)+(z);
			a=result;
			c++;
		}
	System.out.println(c);
	}

}
