a, b = map(int, input().strip().split(' '))
for i in range(b): # 바깥 루프           
    for j in range(a): # 안쪽 루프         
        print('*', end='') 
    print()