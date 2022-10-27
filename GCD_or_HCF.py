a, b = map(int,input().split())
m = a*b
for i in range(1,b+1):
    c = i*a
    if c % b == 0:
        break
print(m//c)