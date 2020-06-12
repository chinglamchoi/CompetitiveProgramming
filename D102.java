import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        float a = Float.parseFloat(s.nextLine().substring(1));
        System.out.println("$" + Math.ceil(a*5)/10);
    }
}
