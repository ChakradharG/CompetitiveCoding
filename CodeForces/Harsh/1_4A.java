import java.util.*;
class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        
        if (num%2 == 0 && num > 2) {
            System.out.println("YES");
        }
        else {
            System.out.println("No");
        }
    }
}