def f(x,y,p):
    if x + y >= 68 or p > 4:
        return p == 4
    if p % 2 != 0:
        return f(x+2,y,p+1) or f(x*2,y,p+1) or\
           f(x,y+2,p+1) or f(x,y*2,p+1)
    else:
        return f(x+2,y,p+1) and f(x*2,y,p+1) and\
           f(x,y+2,p+1) and f(x,y*2,p+1)

for s in range(1,61):
    if f(7,s,1):
        print(s)
        break