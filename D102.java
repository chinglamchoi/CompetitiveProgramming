import java.util.Scanner;
import java.text.DecimalFormat;

public class program {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        a = Float.parseFloat(s.nextLine().substring(1));
        DecimalFormat df = new DecimalFormat("#.#");
        System.out.println("$" + df.format(a/2));
    }
}
