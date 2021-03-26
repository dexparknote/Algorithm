import java.util.*;
/**
 * PS2751
 */
// 버블 소팅으로 풀이 -> 시간 초과! 퀵 소트를 사용해야하나봄.
public class PS2751 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] res = new int[n];
        for(int i=0; i<n; i++) {
            res[i] = sc.nextInt();
        }
        
        int temp = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++) {
                if(res[i] < res[j]) {
                    temp = res[i];
                    res[i] = res[j];
                    res[j] = temp;
                }
            }
        }

        for(int i=0; i<n; i++) {
            System.out.println(res[i]);
        }
    }
    
}