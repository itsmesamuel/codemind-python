n = int(input())
sfc = 0
for i in range(1,n):
    r = n % i
    if r == 0:
        sfc += i
if sfc > n:
    print(True)
else:
    print(False)