#class Person:
#     x=10
#     y=20
#     tup=(1,2,3)
#     c=[2,4,5]
#     d={100,200,300}
#     def func(self):
#         print("this is the my class person")
#         p1=person()
#         p1.func()
#     print(p1.x)
#     print(p1.y)
#     print(p1.tup)
#     print(p1.c)
#     print(p1.d)



class Engine5kcc:
    def __init__(self, kmph,limit):
        self.kmph = kmph
        self.limit = limit

    def Onroad(self, weight):
        print(self.kmph-weight)
        print("Limit is", self.limit)

bmw = Engine5kcc(200,450)
audi = Engine5kcc(100,300)


bmw.Onroad(20)
audi.Onroad(10)



# class Calculation:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
# cal = Calculation()
# print(cal.add(20,10))
# print(cal.sub(20,10))


