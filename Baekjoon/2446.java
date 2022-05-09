import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number;
		number=input.nextInt();
		for(int i=0;i<number;i++) {
			for(int j=(number-i);j<number;j++) {
				System.out.print(" ");
			}
			for(int j=(i*2);j<(number*2)-1;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
		for(int i=1;i<number;i++) {
			for(int j=i;j<number-1;j++) {
				System.out.print(" ");
			}
			for(int j=0;j<2*(i+1)-1;j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}

}
