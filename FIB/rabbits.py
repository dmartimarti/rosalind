def fibonacci(limit,k):
    print 1
    counter = 2
    cn_1 = 1
    cn_2 = 0
    while counter <= limit:
        cn = (cn_2 * (k+1)) + (cn_1 - cn_2)
        print cn
        cn_2 = cn_1
        cn_1 = cn
        counter = counter + 1        
        
def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b

print fib(5,3)