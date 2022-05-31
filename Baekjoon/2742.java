import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int number;
		number=input.nextInt();
		int j=number;
		for(int i=0;i<number;i++) {
			
			System.out.println(j);
			j--;
		}
	}

}
