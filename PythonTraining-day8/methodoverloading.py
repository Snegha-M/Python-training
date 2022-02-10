'''
    Method overloading:
        Methods in Python can be called with zero, one, or more parameters.
        This process of calling the same method in different ways is called method overloading.
        Two methods cannot have the same name in Python
        hence method overloading is a feature that allows the same operator to have different meanings.
'''
# class numbers:
#     def fun(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a + b
#         else:
#             return a
# obj=numbers()
# print("sum:",obj.fun(10))
# print("sum:",obj.fun(10,20))
# print("sum:",obj.fun(10,30,20))
# print("sum:",obj.fun(10,20,30,4))

class numbers:
    def fun(self,*args):
        sum=0
        for i in args:
            sum+=i
        print("sum:",sum)
obj=numbers()
obj.fun(10)
obj.fun(10,20)
obj.fun(10,30,20)
obj.fun(10,20,30,40)
