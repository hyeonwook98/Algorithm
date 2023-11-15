import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        // 우선순위 큐에 우선순위 요소 추가
        for (int i : priorities) {
            queue.add(i);
        }
        // 큐가 빌 때까지 반복
        while (!queue.isEmpty()){
            // 기존 우선순위 배열 순회
            for (int i = 0; i < priorities.length; i++){
                // 현재 작업의 위치 찾기
                if (queue.peek() == priorities[i]){
                    queue.poll();
                    answer++;
                    
                    if (location == i){
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}
