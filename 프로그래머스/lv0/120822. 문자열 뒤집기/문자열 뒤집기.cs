using System;

public class Solution {
    public string solution(string my_string) {
        var answer = my_string.ToCharArray(); // var 생성 하고 char로 변형
        Array.Reverse(answer); // reverse 함
        return new string(answer); // new string array
    }
}

