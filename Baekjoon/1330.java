import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int x;
		int y;
		
		/*System.out.print("첫번째 숫자");*/
		x = input.nextInt();
		/*System.out.print("두번째 숫자");*/
		y = input.nextInt();
		
		if(x>y)
			System.out.println(">");
		else if(x<y)
			System.out.println("<");
		else
			System.out.println("==");
	}

}
