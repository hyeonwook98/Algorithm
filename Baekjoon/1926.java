import java.util.*;
import java.io.*;

public class Main {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static int[][] arr;
  static boolean[][] visited;
  static int max_size = 0;
  static int cnt = 0;
  static int[] dx = {1, 0, -1, 0};
  static int[] dy = {0, 1, 0, -1};

  public static void main(String[] args) throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken()); 
    int m = Integer.parseInt(st.nextToken()); 

    arr = new int[n][m];
    visited = new boolean[n][m];

    // 지도 초기화
    for(int i = 0; i < n; i++){
      st = new StringTokenizer(br.readLine());
      for(int j = 0; j < m; j++){
        arr[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
        if(arr[i][j] == 1 && visited[i][j] == false){
          cnt++;
          max_size = Math.max(max_size, bfs(i,j,n,m));
        }
      }
    }

    System.out.println(cnt);
    System.out.println(max_size);
  }

  public static int bfs(int r, int c, int n, int m){
    Queue<int[]> queue = new LinkedList<>();
    visited[r][c] = true;
    queue.offer(new int[]{r,c});
    int size = 1;

    while (!queue.isEmpty()){
      int[] q;
      q = queue.poll();
      for(int i = 0; i < 4; i++){
        int nx = q[0] + dx[i];
        int ny = q[1] + dy[i];

        if(0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == 1 && visited[nx][ny] == false){
          queue.offer(new int[]{nx,ny});
          visited[nx][ny] = true;
          size++;
        }
      }
    }

    return size;
    
  }
}
