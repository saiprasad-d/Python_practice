N = int(input('Enter the value of N: '))  # input
# calculating 2^N and converting into string
M=str(2**N)
M_new= [i for i in M]
M_final=[int(i) for i in M_new]
answer=sum(M_final)

#if final answer is not of single digit, this loop will be executed
while True:
    if answer > 9:
        ans_str=str(answer)
        M_new= [i for i in ans_str]
        M_final=[int(i) for i in M_new]
        answer=sum(M_final)
        break
    else:
        break
print('Answer to the query is ', answer)
