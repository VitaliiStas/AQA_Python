class Singelton(object):
    obj = None

    def __new__(cls, *dt, **mp):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt, **mp)
        return cls.obj


obj = Singelton()
obj.Attr = 12
print(obj.Attr)


new_obj = Singelton()
new_obj.Attr = 35
print(obj is new_obj)
print(obj.Attr)
print(new_obj.Attr)