class PublicPrivateProtected:
    class_name = 'ClassName2'
    _protected_name = 'PROTECTED'
    __privat_name = 'PRIVAT'


    def __init__(cls, *dt, **mp):
        # print(PublicPrivateProtected.class_name,PublicPrivateProtected._privat_name,PublicPrivateProtected.__protected_name)
        pass

public = PublicPrivateProtected()

print(public.class_name)
# Access to protected var
print(PublicPrivateProtected._protected_name)
# Access to private var
print(public._PublicPrivateProtected__privat_name)
