import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int y;
		int ham,dr;
		int x=input.nextInt();
		for(int i=0;i<2;i++) {
			ham=input.nextInt();
			if(ham<x)
				x=ham;
		}
		y=input.nextInt();
		dr=input.nextInt();
		if(y<dr)
			dr=y;
		System.out.println(x+dr-50);
	}
}
