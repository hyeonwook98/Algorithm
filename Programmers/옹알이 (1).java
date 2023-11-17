import java.util.*;
import java.io.*;
class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        for(int i = 0; i < babbling.length; i++){
            
            if (babbling[i].contains("aya")){
                babbling[i] = babbling[i].replace("aya","0");
            }
            if (babbling[i].contains("ye")){
                babbling[i] = babbling[i].replace("ye","0");
            }
            if (babbling[i].contains("woo")){
                babbling[i] = babbling[i].replace("woo","0");
            }
            if (babbling[i].contains("ma")){
                babbling[i] = babbling[i].replace("ma","0");
            }
            babbling[i] = babbling[i].replace("0", "");

            if (babbling[i].length() == 0){
                answer++;
            }
            
        }
        for(String s : babbling){
            System.out.println(s);
        }
        return answer;

    }
}
