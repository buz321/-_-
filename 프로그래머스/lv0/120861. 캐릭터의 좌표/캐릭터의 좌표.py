def solution(keyinput, board):
    x = 0 
    y = 0
    
    for i in keyinput:
        if i == "right" and x + 1 <= (board[0] //2):
            x += 1
            
        elif i == "left" and x - 1 >= -(board[0] //2):
            x -= 1
            
        elif i == "up" and y + 1 <= (board[1] //2):
            y += 1
            
        elif i == "down" and y - 1 >= -(board[1] //2):
            y -= 1
            
    return [x,y]