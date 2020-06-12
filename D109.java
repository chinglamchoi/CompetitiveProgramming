import java.util.Scanner;
public class D109 {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int b = a.nextInt();
		while (b > 0) {
			if (b >= 1000) {
				System.out.println("1000");
				b -= 1000;
			} else if (b >= 500) {
				System.out.println("500");
				b -= 500;
			} else if (b >= 100) {
				System.out.println("100");
				b -= 100;
			} else if (b >= 50) {
				System.out.println("50");
				b -= 50;
			} else if (b >= 20) {
				System.out.println("20");
				b -= 20;
			} else if (b >= 10) {
				System.out.println("10");
				b -= 10;
			}
		}
	}
}
