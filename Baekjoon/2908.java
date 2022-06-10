import java.io.IOException;
import java.util.Scanner;
public class Main {

		public static void main(String[] args) throws IOException {
			// TODO Auto-generated method stub

			Scanner scan = new Scanner(System.in);
			String s1=scan.next();
			String s2=scan.next();
			
			int a[]= new int [3];
			int b[]= new int [3];
			int r1=0;
			int r2=0;
			//역순으로 배열에넣기
			for(int i=0;i<3;i++) {
				a[2-i]=s1.charAt(i)-'0';
				b[2-i]=s2.charAt(i)-'0';
			}
			//수로 바꾸기
			r1=(a[0]*100)+(a[1]*10)+(a[2]*1);
			r2=(b[0]*100)+(b[1]*10)+(b[2]*1);
			
			if(r1>r2)
				System.out.println(r1);
			else 
				System.out.println(r2);
	}

}
