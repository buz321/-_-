def solution(n, k):
    answer = int((n*12000) + ((k * 2000) - (n//10 * 2000))) # 예로 만약 양꼬치 15인분을 먹으면 n//10으로 1개의 음료수 값을 나타낼수 있음
    return answer