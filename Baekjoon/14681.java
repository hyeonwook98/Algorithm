import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int x;
		int y;
		
		/*System.out.print("첫번째 숫자");*/
		x = input.nextInt();
		y = input.nextInt();
		
		if(x>0&&y>0)
			System.out.println("1");
		else if(x<0&&y>0)
			System.out.println("2");
		else if(x<0&&y<0)
			System.out.println("3");
		else 
			System.out.println("4");
	}

}
