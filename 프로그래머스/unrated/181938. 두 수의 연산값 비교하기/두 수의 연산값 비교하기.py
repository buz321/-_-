def solution(a, b):
    answer = 0
    dap1 = ""
    dap1 = str(a) + str(b)
    dap2 = 2 * a * b
    if int(dap1) >= dap2:
        return int(dap1)
    else:
        return dap2