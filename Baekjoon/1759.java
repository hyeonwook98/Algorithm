import java.util.*;
import java.io.*;

public class Main {
    static int l,c;
    static Character[] arr;
    static Character[] mo = new Character[]{'a','e','i','o','u'};
    static List<String> result = new ArrayList<>();
    
    public static void main(String args[]) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      l = Integer.parseInt(st.nextToken());
      c = Integer.parseInt(st.nextToken());
      
      arr = new Character[c];
      
      st = new StringTokenizer(br.readLine());
      for(int i=0; i<c; i++){
          arr[i] = st.nextToken().charAt(0);
      }
      
      Arrays.sort(arr);
      
      dfs(0, "", 0, 0);
      
      for(String s : result){
          System.out.println(s);
      }
    }
    
    static void dfs(int idx, String key, int ja_num, int mo_num){
        if (idx >= c)
            return;
            
        key += (char) arr[idx];
        String chk = "mo";
        
        if (Arrays.asList(mo).contains(arr[idx])){
            mo_num++;
        } else{
            chk = "ja";
            ja_num++;
        }
        
        if(key.length() == l && mo_num >= 1 && ja_num >= 2){
            result.add(key);
        }
        
        dfs(idx + 1, key, ja_num, mo_num);
        if (chk.equals("mo")){
            dfs(idx + 1, key.substring(0,key.length() - 1), ja_num, mo_num - 1);
        } else{
            dfs(idx + 1, key.substring(0,key.length() - 1), ja_num - 1, mo_num);
        }
    }
}
