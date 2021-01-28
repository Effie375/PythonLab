def sayHello(onoma="Human"):
    print("Hello %s" % onoma)


def modDiv(x, y):
    mod = x % y
    div = x // y
    return mod, div


# -------main--------
sayHello()
sayHello("Chris")
a, b = modDiv(10, 3)
