import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int score;
		int sum=0;
		for(int i=0;i<5;i++) {
			score=input.nextInt();
			if(score<40)
				score=40;
			sum=sum+score;
		}

		System.out.println(sum/5);
	}

}
