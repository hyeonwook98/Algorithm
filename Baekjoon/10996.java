import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number;
		number=input.nextInt();
		for(int x=1;x<number+1;x++) {
			
		
			for(int i=2;i<=number+1;i++) {
			if(i%2==1)
			    System.out.print(" ");
			if(i%2==0)
				System.out.print("*");
			}
		
		    System.out.println("");
		
		
		    for(int j=2;j<=number+1;j++) {
			if(j%2==1)
				System.out.print("*");
			if(j%2==0)
				System.out.print(" ");
		    }
		
		    System.out.println("");
		}
	}

}
