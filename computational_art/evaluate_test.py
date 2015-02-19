import math
def evaluate(f, x, y):
    if f!=['x'] and f!=['y']:
        if f[0]=='prod':
            return evaluate(f[1],x,y)*evaluate(f[2],x,y)
        elif f[0]=='ave':
            return .5*(evaluate(f[1],x,y)+evaluate(f[2],x,y))
        elif f[0]=='cos':
            return math.cos(3.14159*evaluate(f[1],x,y))
        elif f[0]=='sin':
            return math.sin(3.14159*evaluate(f[1],x,y))
        elif f[0]=='neg':
            return -1*evaluate(f[1],x,y)
        elif f[0]=='dif':
            return abs(evaluate(f[1],x,y))-abs(evaluate(f[2],x,y))      
    elif f==['x']:
        return x
    elif f==['y']:
        return y
    else:
        print 'invalid string'


print evaluate(['dif',['x'], ['y']],1,.5)