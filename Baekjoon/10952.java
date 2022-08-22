import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int number1;
		int number2;
		number1=input.nextInt();
		number2=input.nextInt();
		while((number1!=0)&&(number2!=0)) {
			System.out.println(number1+number2);
			number1=input.nextInt();
			number2=input.nextInt();
		}
	}

}
