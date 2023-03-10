n = int(input())
x = 1
y = 0
while x <= n:
    p = pow(-1, x-1)
    q = 1/x
    y = y + p*q
    x += 1
print(y)