import java.util.*;
import java.io.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        // 힙 초기화
        for(int i = 0; i < scoville.length; i++){
           heap.add((Integer) scoville[i]);
        }
        
        while (true){
            if (heap.peek() >= K)
                break;
            
            if (heap.size() <= 1)
                return -1;
            
            Integer f = heap.poll();
            Integer s = heap.poll();
            
            Integer suffle_scoville = f + (s*2);
            heap.add(suffle_scoville);
            answer ++;
        }
        
        return answer;
    }
}
