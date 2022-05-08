import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int number;
		number=input.nextInt();
		
		for(int i=1;i<=number;i++) {
			for(int a=0;a<number-i;a++) {
				System.out.print(" ");
			}
			for(int j=0;j<i;j++) {
				System.out.print("*");
			}
			System.out.println("");
			
		}
	}

}
