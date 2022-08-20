import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number;
		int x,y;
		
		number=input.nextInt();
		for (int i=0;i<number;i++) {
			x=input.nextInt();
			y=input.nextInt();
			System.out.println(x+y);
		}
	}

}
