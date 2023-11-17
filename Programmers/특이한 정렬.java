import java.util.*;
import java.io.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        int[] answer = new int[numlist.length];
        
        ArrayList<int[]> arr = new ArrayList<>();
        
        for(int i=0; i<numlist.length; i++){
            int[] tmp = new int[2];
            tmp[0] = Math.abs(numlist[i] - n);
            tmp[1] = numlist[i];
            arr.add(tmp);
        }
                              
        Collections.sort(arr, (a,b) -> {
            if (a[0] == b[0]){
                return b[1] - a[1];
            } else{
                return a[0] - b[0];
            }
        });
                              
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i)[1];
        }                      
                              
        return answer;
    }
}
