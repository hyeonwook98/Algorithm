import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> map = new HashMap();
        // 전화번호부 돌면서 해시맵에 저장
        for (int i = 0; i < phone_book.length; i++){
            map.put(phone_book[i], 0);
        }
        // 전화번호부 돌면서 접두어가 다른 번호에 있으면 false 반환
        for (int i = 0; i < phone_book.length; i++){
            for(int j = 1; j < phone_book[i].length(); j++) {
                if (map.containsKey(phone_book[i].substring(0,j))) {
                    return false;
                }
            }
        }
        // 접두어가 없는 경우 true 반환
        return true;
    }
}
