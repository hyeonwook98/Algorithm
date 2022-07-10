import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner input = new Scanner(System.in);
		int count = 0;
		int sum = 0;

		int number = input.nextInt();
		String s[] = new String[number];

		for (int i = 0; i < number; i++) {
			s[i] = input.next();
			for (int j = 0; j < s[i].length(); j++) {
				if (s[i].charAt(j) == 'O') {
					count++;
					sum += count;
				} else
					count = 0;
			}
			System.out.println(sum);
			count = 0;
			sum = 0;
		}

        input.close();
	}
}
