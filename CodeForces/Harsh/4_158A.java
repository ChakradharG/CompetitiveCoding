import java.util.*;
class Main {
    
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String []num = sc.nextLine().split(" ");
        int len = Integer.parseInt(num[0]);
        int position = Integer.parseInt(num[1]);
        int count = 0;
     
        String []scores = sc.nextLine().split(" ");
        int minScore = Integer.parseInt(scores[position - 1]);
        int currentCount = 0;
        for(String i: scores) {
            if ((Integer.parseInt(i) != 0) && Integer.parseInt(i) >= minScore ) count++;
        }
        
        System.out.println(count);
    }
}