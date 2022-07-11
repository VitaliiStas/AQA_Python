class ClassName2:
    class_name = 'ClassName2'
    _privat_name = 'PRIVAT'
    __protected_name = 'PROTECTED'

    def __init__(self):
        pass

    def m1(self):
        print("Your input from the "+str(self.class_name))


var1 = ClassName2

var1.m1(var1)

