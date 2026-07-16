a=98
def f1():
    a = 85
    def f2(a):
        print(a)
    return f2()
myansr = f1()

