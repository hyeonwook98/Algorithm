import java.io.IOException;
import java.util.Scanner;
public class Main {

		public static void main(String[] args) throws IOException {
			// TODO Auto-generated method stub

			Scanner scan = new Scanner(System.in);
			String s=scan.next();
			int a[]= new int[26];
			int time=0;
			//해당알파벳에 맞는시간넣기
			for(int i=0;i<26;i++) {
				if(0<=i&&i<=2)
					a[i]=3;
				else if(3<=i&&i<=5)
					a[i]=4;
				else if(6<=i&&i<=8)
					a[i]=5;
				else if(9<=i&&i<=11)
					a[i]=6;
				else if(12<=i&&i<=14)
					a[i]=7;
				else if(15<=i&&i<=18)
					a[i]=8;
				else if(19<=i&&i<=21)
					a[i]=9;
				else if(22<=i&&i<=25)
					a[i]=10;
			}
			for(int i=0;i<s.length();i++) {
				time=time+a[s.charAt(i)-65];
			}
		    System.out.println(time);
	}

}
