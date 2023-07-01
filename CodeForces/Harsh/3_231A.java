import java.util.*;
class HelloWorld {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int mainCount = 0;
        for (int i=0; i<n; i++) {
            String []nums = sc.nextLine().split(" ");
            int count = 0;
            for(String p: nums) {
                if (p.equals("1")) count++;
            }
            
            if (count >= 2) mainCount++;
            
        }
        
        System.out.println(mainCount);
    }
}