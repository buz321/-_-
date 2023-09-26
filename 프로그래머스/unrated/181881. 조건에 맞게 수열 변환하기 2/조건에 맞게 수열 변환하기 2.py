def solution(arr):
    idx = 0
    prev = arr
    
    while True:
        apx = []
        for i in prev:
            if i >= 50 and i % 2 == 0: 
                apx.append(int(i / 2))
            elif i < 50 and i % 2 == 1: 
                apx.append(i * 2 + 1)
            else: apx.append(i)

        same = all(a == b for a, b in zip(prev, apx))
        if same:
            break
        idx += 1

        prev = apx
    
    return idx