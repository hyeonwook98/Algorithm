import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int year;
		
		
		/*System.out.print("첫번째 숫자");*/
		year = input.nextInt();
		
		if(((year%4)==0)&&((year%100)!=0))
			System.out.println("1");
		else if((year%4)==0&&((year%400)==0))
			System.out.println("1");
		else
			System.out.println("0");
	}

}
