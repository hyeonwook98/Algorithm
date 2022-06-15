import java.util.HashSet;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		
		HashSet<Integer> set = new HashSet<Integer>();
		
		int s[] = new int[10];
		for(int i=0;i<s.length;i++) {
			s[i]=input.nextInt()%42;
			set.add(s[i]);
		}
		System.out.print(set.size());
	}
}
