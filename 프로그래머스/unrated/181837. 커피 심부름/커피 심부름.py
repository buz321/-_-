def solution(order):
    answer = 0
    order_str = ' '.join(order)
    for i in order_str.split():
        if 'americano' in i or 'anything' in i:
            order_str = order_str.replace(i, '4500')
            answer += 4500
        elif 'cafelatte' in i:
            order_str = order_str.replace(i, '5000')
            answer += 5000

            
    return answer
