import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		double sum=0;
		double avg=0;
		double result=0;
		int tc = input.nextInt();
		for(int i=0;i<tc;i++) {
			int number=input.nextInt();
			int s[]=new int[number];
			int count=0;
			
			for(int j=0;j<number;j++) {
				
				s[j]=input.nextInt();
				sum+=s[j];
			}
			avg=sum/number;
			for(int j=0;j<number;j++) {

				if(s[j]>avg) {
					count++;
				}
				
			}
			result=(double)count/number*100;
			sum=0;
			
			System.out.print(String.format("%.3f",result));
			System.out.println("%");
		}
	}
}
