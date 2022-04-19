import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		int number = input.nextInt();
		int s[] = new int [number];
		double s2[] = new double[number];
		int max=0;
		double sum=0;
		for(int i=0;i<number;i++) {
			s[i]=input.nextInt();
			if(max<s[i]) {
				max=s[i];
			}
		}//완료
		for(int i=0;i<number;i++) {
			s2[i]=(double)s[i]/max*100;
		}
		for(int i=0;i<number;i++) {
			sum+=s2[i];
		}
		System.out.print(sum/number);
	}
}
