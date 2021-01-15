def apot(x):
    return x % 2


def foo(n):
    apot1 = n * 2
    n = apot1 * 2
return n, apot1

a = int(input("Δώσε αριθμό: ").strip())

if apot(a) == 0:
    a, n = foo(a)
    print(a, n)
else:
    print(apot(a))
