import java.util.Scanner;
public class program {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        int b = a.nextInt();
        String s = Integer.toString(b);
        if (!((b % 100 == 11) || (b % 100 == 12) || (b % 100 == 13))) {
            switch(s.substring(s.length()-1, s.length())) {
                case "1":
                    System.out.println(s + "st");
                    break;
                case "2":
                    System.out.println(s + "nd");
                    break;
                case "3":
                    System.out.println(s + "rd");
                    break;
                default:
                    System.out.println(s + "th");
                    break;
            }
        } else {
            System.out.println(s + "th");
        }
    }
}
