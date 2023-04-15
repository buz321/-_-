def solution(hp):
    janggoon = hp // 5
    byeongjeong = (hp - (5*janggoon)) // 3
    ilban = (hp-(5*janggoon)-(3*byeongjeong))//1
    return janggoon+byeongjeong+ilban

