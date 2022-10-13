n =  int(input())
t = n
s = n * n
d = 0
while n > 0:
    n = n // 10
    d += 1
x = s % 10 ** d
if x == t:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')