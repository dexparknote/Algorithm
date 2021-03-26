import java.util.*;
// 퀵 소트도 시간 초과가 뜬다..
public class PS2751_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();

        ArrayList<Integer> list = new ArrayList<>();

        for(int i=0; i<n; i++) {
            list.add(sc.nextInt());
        }

        Collections.sort(list);

        for(int i : list) {
            sb.append(i).append('\n');
        }
        System.out.println(sb);
    }
}
