import java.util.*;
import java.io.*;

public class Main {
    static int n, s;
    static int cnt;
    static int sum_result = 0;
    static int idx = 0;
    static int[] arr;
    
    public static void main(String args[]) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      s = Integer.parseInt(st.nextToken());
      
      arr = new int[n];
      st = new StringTokenizer(br.readLine());
      
      for(int i=0; i<n; i++){
          arr[i] = Integer.parseInt(st.nextToken());
      }
      
      dfs(idx, sum_result);
      
      System.out.println(cnt);
    }
    
    static void dfs(int idx, int sum){
        if (idx >= n)
            return;
            
        sum += arr[idx];
        
        if (sum == s)
            cnt++;
            
        dfs(idx + 1, sum - arr[idx]);
        dfs(idx + 1, sum);
    }
}
