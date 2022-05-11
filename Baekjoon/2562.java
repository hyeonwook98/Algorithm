import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		
		int[] s = new int[9];
		int max;
		int number=1;
		for(int i=0;i<9;i++) {
			s[i]=input.nextInt();
		}
		max=s[0];
		
		for(int i=1;i<9;i++) {
			if(max<s[i]) {
				max=s[i];
				number=i+1;
			}
		}
		System.out.println(max);
		System.out.print(number);
	}

}
