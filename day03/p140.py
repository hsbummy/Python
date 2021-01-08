# data = 100

def calcsum(n):
    sum = 0
    for x in n:
        sum += x
    return sum;


def f1():
    data = 100
    return data

def f2(s, e):
    sum = 0
    for data in range(s, e+1):
        sum += data

    return sum / int(e-s+1)

def f3(s, e):
    sum = 0
    for data in range(s, e+1):
        sum += data
    print('result : ')
    print(sum / int(e-s+1))

def f4(*n):
    sum = 0
    for d in n:
        sum += d;
    return sum

def f5(m, *n):
    sum = 0
    for d in n:
        sum += d;
    return sum + m;

# 불변인자가 앞에, 가변인자가 뒤에

def f6(begin=1, end=2, step=1):
    sum = 0;
    '''begin : start data... default value =1'''
    for d in range(begin, end+1, step):
        sum += d;
    return sum

def f7(**args):
    b = args['b'];
    e = args['e'];
    s = args['s'];
    sum = 0;
    for d in range(b, e + 1, s):
        sum += d;
    return sum

def f8(n, *m, **a):
    print(n, 'test');
    print(n)
    print(m)
    print(a)