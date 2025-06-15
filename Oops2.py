# #Del keyyword

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("sanjay")
# print(s1.name)
# del s1.name
# print(s1.name)

# # Private(like) attributes & methods 

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #private

#     def reset_pass(self):
#         print(self.__acc_pass)

# s1 = Account("12345","abcde")
# print(s1.acc_no)
# print(s1.reset_pass())

# # print(s1.__acc_pass)

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())


# #Inheritance
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(Car):          
#     def __init__(self, name):
#         self.name = name

# c1 = ToyotaCar("fortuner")
# c2 = ToyotaCar("prius")

# print(c1.start())
# print(c1.stop())

# #METHOD-2(Multiple)
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(Car):          
#     def __init__(self, brand):
#         self.name = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# c1 = Fortuner("diesel")
# print(c1.type)
# c1 = ToyotaCar("fortuner")
# c2 = ToyotaCar("prius")

# print(c1.start())
# print(c1.stop())

# #Multi-Level Inheritance
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)


# #SUPER METHOD
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(Car):          
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# c1 = ToyotaCar("prius", "electric")
# print(c1.type)


# there are three types of method:
# # 1. static methods
# # 2. class methods(class) 
# # 3. instance methods(self)
 


# #CLASS METHOD
# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     self.name = name
#         # self.__class__.name = "Rahul"
#         # self.__class__.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)