/**
 * PS1260
 */
import java.util.*;

import jdk.javadoc.internal.tool.resources.version;

public class PS1260 {
    static int[][] chk; // 간선 연결상태
    static boolean[] chked; // 확인 여부
    static int n; //정점 개수
    static int m; //간선 개수
    static int v; //시작 정점
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();

        chk = new int[1001][1001];
        chked = new boolean[1001];

        for(int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            chk[x][y] = chk[y][x] = 1;
        }

        dfs(v);

        chked = new boolean[1001];
        System.out.println();

        bfs();
    }

    public static void dfs(int i) {
        chked[i] = true;
        System.out.print(i + " ");

        for(int j=1; j<=n; j++) {
            if(chk[i][j] == 1 && chked[j] == false) {
                dfs(j);
            }
        }
    }

    public static void bfs() {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(v); //시작점 큐에 넣어야 함
        chked[v] = true;
        System.out.print(v + " ");

        //큐가 빌 때까지 반복. 방문 정점은 확인, 출력 후 큐에 넣어 순서대로 확인
        while(!queue.isEmpty()) {
            int temp = queue.poll();

            for(int j=0; j<=n; j++) {
                if(chk[temp][j] == 1 && chked[j] == false) {
                    queue.offer(j);
                    chked[j] = true;
                    System.out.print(j + " ");
                }
            }
        }
    }
}