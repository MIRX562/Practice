from re import X


def fpb(a,b):
    if b==0:
        return a
    else:
        return fpb(b,a%b)
x = fpb(45,20)
print(x)