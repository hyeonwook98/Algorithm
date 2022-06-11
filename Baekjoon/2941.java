//배열 인덱스넘어가는거조심
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		Scanner scan = new Scanner(System.in);
		String s = scan.nextLine();
		int count = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == '-' || s.charAt(i) == '=') {
			} else if (s.charAt(i) == 'c') {
				if (i < s.length() - 1) {
					if (s.charAt(i + 1) == '-' || s.charAt(i + 1) == '=') {
						i = i + 1;
					}
				}
			} else if (s.charAt(i) == 'd') {
				if (i < s.length() - 1) { // 인덱스범위넘어가는것조심

					if (s.charAt(i + 1) == '-') {
						i = i + 1;
					} else if (s.charAt(i + 1) == 'z') {
						if (i < s.length() - 2) {// 인덱스범위넘어가는것조심
							if (s.charAt(i + 2) == '=') {
								i = i + 2;
							}
						}
					}
				}
			} else if (s.charAt(i) == 'l') {
				if (i < s.length() - 1) {
					if (s.charAt(i + 1) == 'j') {
						i = i + 1;
					}
				}
			} else if (s.charAt(i) == 'n') {
				if (i < s.length() - 1) {
					if (s.charAt(i + 1) == 'j') {
						i = i + 1;
					}
				}
			} else if (s.charAt(i) == 's') {
				if (i < s.length() - 1) {
					if (s.charAt(i + 1) == '=') {
						i = i + 1;
					}
				}
			}

			else if (s.charAt(i) == 'z') {
				if (i < s.length() - 1) {
					if (s.charAt(i + 1) == '=') {
						i = i + 1;
					}
				}
			}
			count++;
		}
		System.out.println(count);
	}
}
