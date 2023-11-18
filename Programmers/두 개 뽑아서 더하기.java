import java.util.*;
import java.io.*;
class Solution {
    static HashSet<Integer> answer;

    public ArrayList<Integer> solution(int[] numbers) {
        
        answer = new HashSet<>();
        
        combinations(numbers,0,0,0);
        ArrayList<Integer> result = new ArrayList<>(answer);
        Collections.sort(result);
        
        return result;
    }
    
    static void combinations(int[] numbers, int idx, int depth, int sum){
        if (depth == 2){
            answer.add(sum);
            return;
        }
        
        if (idx >= numbers.length){
            return;
        }
        
        combinations(numbers, idx+1, depth+1, sum+numbers[idx]);
        combinations(numbers, idx+1, depth, sum);

    }
    
}
