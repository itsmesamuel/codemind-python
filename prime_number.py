n = int(input())
sfc = 0
for i in range(1,n+1):
    r = n % i
    if r == 0:
        sfc += 1
if sfc == 2:
    print('prime')
else:
    print('not a prime')