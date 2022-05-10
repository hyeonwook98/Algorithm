import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number;
		number=input.nextInt();
		for(int i=0;i<number;i++) {
			for(int j=0;j<=i;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
		for(int i=0;i<number-1;i++) {
			for(int j=i;j<number-1;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}

}
