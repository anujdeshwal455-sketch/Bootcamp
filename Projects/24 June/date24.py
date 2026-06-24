# class methods & static method
class  Employee:
    company ="krm corp"
    _count = 0

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        Employee._count += 1

    @classmethod
    def get_count(cls):
         return f"{cls.compnay} has {cls._count} employees"
         
    @staticmethod
    def validate_dept(dept):
        valid = ["CDE", "ECE", "MBA", "MCA"]
        return dept in valid
e1 = Employee("alice", "CSE")
print(Employee.get_count())
e2 = Employee("Bob", "ECE")
print(Employee.validate_dept("CSE"))






from tkinter import dnd


class Student:
    total_students = 0

    def __init__(self, roll_no, marks, grade):
        self.__roll_no = roll_no
        self.__marks = []
        self.marks = marks 
        self._grade = grade

        Student.total_students += 1

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks_list):
        for mark in marks_list:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks_list

    @property
    def gpa(self):
        avg_marks = sum(self.__marks) / len(self.__marks)
        return avg_marks / 10
    @classmethod
    def count(cls):
        return cls.total_students
s1= Student(101, [80, 90, 85], "b")
s2 = Student(102, [70, 75, 80], "c")

print("Student 1 GPA:", s1.gpa)
print("Student 2 GPA:", s2.gpa)
print("Total Students:", Student.count())











class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn         
        self._title = title         
        self._author = author     

        if copies < 0:
            raise ValueError("Copies cannot be negative")
        self.__copies = copies     

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__copies

    def checkout(self, n):
        if n <= 0:
            raise ValueError("Checkout quantity must be positive")

        if n > self.__copies:
            raise ValueError("Not enough copies available")

        self.__copies -= n

    def return_book(self, n):
        if n <= 0:
            raise ValueError("Return quantity must be positive")

        self.__copies += n


book = Book("9781234567890", "Python Basics", "John Doe", 5)

print("Available copies:", book.available)

book.checkout(2)
print("After checkout:", book.available)

book.return_book(1)
print("After return:", book.available)

print("ISBN:", book.isbn)





# class xyz extends abc;
#     def_init_(self, c, d):
#         self = c
#         self = d
#     def any_method()
#     print("_") 




class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def study(self):
        print("Studying")

s = Student("Anuj")
s.display()
s.study()







# Multilevel Inheritance
 
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
     def bark(self):
        print("Barking")
class puppy(Dog):
    def weep(self):
        print("weeping")

p = puppy()
p.puppy()
p.bark()
p.weep()