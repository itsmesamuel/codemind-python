n = int(input())
p = 1
s = 0
while n > 0:
    r = n % 10
    p = p * r
    s = s + r
    n = n // 10
print(p-s)