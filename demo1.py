class A:
    v=100
    def __init__(self):
        self.v=200

a1=A()
a2=A()
del a2.v
print(A.v)          # 通过类访问类变量100
print(a1.v)         #对象有实例变量时，优先返回实例变量200
print(a2.v)         #实例变量被删除，才返回类变量100
print(a1.__class__.v)#用__class__通过对象访问类变量100 (不建议)



