def solution(board, moves):
    bucket = [] # 바구니 리스트 생성
    answer = [] # 정답 리스트 생성
    for move in moves: 
        for i in range(len(board)): # range 값을 고려 한 -1
            if board[i][move-1] > 0: # 0이 아닌 숫자가 나오면
                bucket.append(board[i][move-1]) # 버켓에 숫자를 추가
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]: # 만약 버켓에 있는 캐릭터(?)가 연속으로 같으면  (맨뒤에서 연속)
                    answer += bucket[-1:] # answer 값에 마지막에 나온 값을 추가
                    bucket = bucket[:-2] # 그리고 버켓은 그 연속된 값을 빼고 저장함
                break
    return len(answer)*2 # 값을 저장할때 중복을 하나의 값을 저장했기에 곱하기 2
