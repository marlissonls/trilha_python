class A:
    def m1(self):
        print('método de A')

class B(A):
    def m1(self):
        super().m1()

    def m2(self):
        print('método de B')

class C(A):
    def m1(self):
        super().m1()

    def m2(self):
        print('método de C')

class D(B, C):
    def m1(self):
        super().m1()

    def m2(self):
        super().m2()