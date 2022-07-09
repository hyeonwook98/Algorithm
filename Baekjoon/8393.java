import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number;
		int sum=0;
		
		number=input.nextInt();
		for (int i=1;i<=number;i++) {
			sum=sum+i;
			
			
		}
		System.out.println(sum);
	}

}
