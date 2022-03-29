import java.util.Scanner;

public class Main {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int number = input.nextInt();
		
		int count=0;
		if ((number) < 100)
			System.out.print(number);
		
		else {
			if(number==1000)
				number=999;
			for (int i = 100; i <= number; i++) {

				
				if(math(i)==1)
					count++;

			}
			
			System.out.print(99+count);
		}
		
	}
	static int math(int a) {
		
		int x = a / 100;
		int y = (a % 100) / 10;
		int z = a % 10;
		if ((y-x)==(z-y)) {
			return 1;
		}
		return 0;
	}
}
