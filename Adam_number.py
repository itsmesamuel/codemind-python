n = int(input())
n2 = n * n
rev_n = 0
while n >0:
    r = n % 10
    rev_n = rev_n * 10 + r
    n = n // 10
k = rev_n
k2 = k * k
rev_k2 = 0
while k2 > 0:
    r = k2 % 10
    rev_k2 = rev_k2 * 10 + r
    k2 = k2 // 10
if rev_k2 == n2:
    print(True)
else:
    print(False)