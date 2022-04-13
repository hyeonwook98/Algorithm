import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int n;
		int count = 0;
		int result = 0;
		Scanner scan = new Scanner(System.in);
		n = scan.nextInt();
		String a[] = new String[n];
		int b[] = new int[26];
		for (int i = 0; i < n; i++) {
			a[i] = scan.next();
		}
		for (int i = 0; i < n; i++) {
			for (int q = 0; q < 26; q++) {  //알파벳에대응하는값설정
				b[q] = 0;
			}
			for (int j = 0; j < a[i].length(); j++) { //i와i+1이 다르면 b배열에 ++
				if (j + 1 != a[i].length()) {
					if (a[i].charAt(j) != a[i].charAt(j + 1)) {
						b[a[i].charAt(j) - 97]++;
					}
				}
				else     //단 값이같다가 마지막까지간경우
					b[a[i].charAt(j) - 97]++;
			}
		
			for (int j = 0; j < 26; j++) {
				if (b[j] >= 2)
					count++;
			}
			if (count == 0)
				result++;
			count=0;
		}
		
		System.out.println(result);
	}
}
