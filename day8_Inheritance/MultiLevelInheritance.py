class P1:
    def m1(self):
        print("Parent 1 method")

class P2(P1):

    def m1(self):
        print("Parent 2 method")

class P3(P2):

    def m1(self):
        print("Parent 3 method")


obj1=P3()
obj1.m1()

