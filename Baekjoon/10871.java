import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int number;
		int min;
		number=input.nextInt();
		min=input.nextInt();
		
		for(int i=0;i<number;i++) {
			int number2=input.nextInt();
			if(number2<min) {
				System.out.print(number2+" ");
			}
		}
	}

}
