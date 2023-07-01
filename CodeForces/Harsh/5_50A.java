import java.util.*;
class HelloWorld {
    
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String []num = sc.nextLine().split(" ");
        int n = Integer.parseInt(num[0]);
        int m = Integer.parseInt(num[1]);
        
        
       
        System.out.println((int)Math.floor((n*m)/2));
    }
}