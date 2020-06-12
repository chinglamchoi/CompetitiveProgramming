import java.util.Scanner;
public class program {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = Integer.parseInt(s.nextLine());
        System.out.println(a < 40000000 ? "Fixed" : "Mobile");
    }
}
