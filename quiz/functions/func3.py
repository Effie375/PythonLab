def x(n):
    if n == 2:
        return n
    else:
        return x(n-1)

print(x(3))

