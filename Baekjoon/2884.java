import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int h;
		int m1;
		int m2;
		
		/*System.out.print("첫번째 숫자");*/
		h = input.nextInt();
		m1 = input.nextInt();

		m2=m1-45;
		if(m2<0) {
			h=h-1;
			m2=15+m1;
			if(h<0) {
				h=23;
			}
		}	
		System.out.println(h+" "+m2);
	}

}

