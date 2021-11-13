class A:
    vc = 123
    def __init__(self):
        pass


n1 = A()
n2 = A()
A.vc = "Mudei"
print(n1.vc)
print(n2.vc)
print(A.vc)