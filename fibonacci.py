import time
def fib(stop):
    if stop < 0:
        negStart = [0, -1]
        for digit in range(abs(stop)):
            negStart.append(negStart[0] + negStart[1])
            negStart.pop(0)
        print(negStart[0])
    else:
        start = [0, 1]
        for digit in range(stop):
            start.append(start[0] + start[1])
            start.pop(0)
        print(start[0])
    pass

fib(int(input('Enter the positive or negative number of times you would like the Fibonacci Sequence to itterate!\nNegative numbers will return the negative Fibonacci.\n>')))
time.sleep(5)
'''
Thomas's assistance twords negative fib
#        fib(n)    =             fib(n-1)         +            fib(n-2)
#        fib(n)    =             fib(n+1)         -            fib(n+2)
'''
'''
Old else statement
for index,digit in enumerate(list(range(stop))):
    start.append(start[index] + start[index + 1])
'''
'''
elif stop == 1:
    print(1)
elif stop == -1:
    print(-1)
'''
'''
if stop == 0 or stop == 1 or stop == -1:
    print(stop)
'''
