# class shape:
#     def area(self):
#         print("area of the shape")

# class Rectangle:
#     def area(self):
#         print("area of rectangle = length x breadth")

# s=shape()
# s.area()

# s=Rectangle()
# s.area()

# from abc import ABC, abstractmethod
# class Car(ABC):
#     def Profit(self):
#         pass

# class Hyundai:
#     def Profit(self):
#         print("Hyundai car is sold with the profit of 25% ")


# b= Car()
# b.Profit()

# a= Hyundai()
# a.Profit()

# a=int(input("Enter a numberator"))
# b=int(input("Enter a denominator"))

# try:
#     print(a/b)

# except Exception:
#     print("can't divide by 0")


# a=int(input("Enter a numberator"))
# b=int(input("Enter a denominator"))

# try:
#     print(a/b)

# except Exception as e:
#     print("can't divide by 0",e)




# try:
#     a=int(input("Enter a numberator"))
#     b=int(input("Enter a denominator"))
#     print(a//b)

# except ZeroDivisionError:
#     print("can't divide by 0")
# except ValueError:
#     print("Enter correct type of value")
# except Exception:
#     pass
# finally:
#     print("hi")


# class Acc:
#     a = 20
#     _b = 30
#     __c = 40

# class oft(Acc):
#     pass
# class c:
#     def z(self):
#         print (self.__c)
# obj = c()
# print(obj.a)
# print(obj.b)


# num = [1,2,4,5,6,7]
# add=list(filter(lambda a: a%2 == 0, num))


# print(add)

# import numpy as np
# arr = np.array([10,20,30])
# print(arr)
# z=np.zeros(5)
# print(z)
# o = np.ones(5)
# print(o)
# ar = np.arange(1,10,2)
# print(ar)

