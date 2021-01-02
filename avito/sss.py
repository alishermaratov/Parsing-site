a = 9876
c = a//60
b = a%60
if c > 72:
    c=c-72
elif c > 48:
    c=c-48
elif c >=24:
    c=c-24
else:
    c


print(c, b)
