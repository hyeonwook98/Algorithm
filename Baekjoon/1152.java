import java.io.IOException;
import java.util.Scanner;
public class Main {

		public static void main(String[] args) throws IOException {
			// TODO Auto-generated method stub

			Scanner scan = new Scanner(System.in);
			String s=scan.nextLine();
			s=s.trim();
			String[] split=s.split(" ");
			int count=split.length;
			if(s.isEmpty()) {
				System.out.println(0);
			}
			else
			System.out.println(count);
	}

}
