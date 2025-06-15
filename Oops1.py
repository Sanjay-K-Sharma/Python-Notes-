# # basic opps class and object
# class Student:
#     name="sanjay"
#     age="alia"
# s1=Student()
# print(s1.name)
# print(s1.age)

# class Car:
#     color="blue"
#     brand="mercedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)

##constractor
# class Student:

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("addint new student in Database..")

# s1=Student("sanjay",98)
# print(s1.name)

# s2=Student("alia")
# print(s2.name)

# #attributes
# class Student:
#     college_name="ABC college"
#     name="anonymous" #class attributes

#     def __init__(self,name,marks):
#         self.name=name #obj attr > class attr
#         self.marks=marks
#         print("addint new student in Database..")

# s1=Student("sanjay",98)
# print(s1.name)
# print(s1.college_name)

#METHOD
# class Student:
#     college_name="ABC college"
#     name="anonymous" #class attributes

#     def __init__(self,name,marks):
#         self.name=name #obj attr > class attr
#         self.marks=marks
#         print("addint new student in Database..")
#     def welcome(self):
#         print("welcome student,")
#     def get_marks(self):
#         return self.marks

# #QUESTION:
#          Create student class that takes name and marks of 3 subjects as arguments in constractor.
#          Then create a method to print the average.
 
# s1=Student("sanjay",98)
# print(s1.name)
# print(s1.college_name)
# s1.welcome()
# print(s1.get_marks())

# #Practice Question 
# class Student:
#     student_name="Name- Sanjay Sharma"
#     def __init__(self, sub_name, sub_marks):
#         self.sub_name=sub_name #obj attr > class attr
#         self.sub_marks=sub_marks

# s1=Student("physics-",98)
# print(s1.student_name)
# print(s1.sub_name)
# print(s1.sub_marks)

# s2=Student("maths-",98)
# print(s2.sub_name)
# print(s2.sub_marks)

# s3=Student("chemistry-",98)
# print(s3.sub_name)
# print(s3.sub_marks)

# # Dushara Mathod
# class Student:
#     def __init__(self, name, marks):
#         self.name= name 
#         self.marks= marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("tony stark", [99,98,97])
# print(s1.name)
# print(s1.marks)
# s1.get_avg()

# # ABSTRACTION

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False 
         
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()

# #PRACTICE QUESTION
# class Bank:
#     def __init__(self, acc, bal):
#         self.balance = acc
#         self.account_no = bal

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance =", self.get_balance())


#     def get_balance(self):
#         return self.balance

# s1 = Bank(10000, 12345678)
# s1.debit(10000)
# s1.credit(500)
# s1.credit(40000)
# s1.debit(10000)

