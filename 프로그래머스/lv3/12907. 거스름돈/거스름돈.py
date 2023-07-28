def solution(n, money):
    result = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            result[i] = (result[i] + result[i-m]) % 1000000007
    return result[n]