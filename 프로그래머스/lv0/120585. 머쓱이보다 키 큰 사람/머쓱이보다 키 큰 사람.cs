using System;

public class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        foreach (var i in array) {
            if (i > height) {
                answer += 1;
            }
        }
        return answer;
    }
}

