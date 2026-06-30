class shap:
    def __init__(self, color="white"):
        self.color = color
        def area(self):
            return 0
        def describe(self):
            return
        




# MRO - method resoulution order
class A:
            def greet (self): return "Hello from  A"
class B(A):
      def greet(self):return "Hello from  B"
class C(A):
    def greet(self): return "Hel__mro__])lo from  C"
class D(B, C):
        pass
d = D()
print(d.greet())
print(D.__mor__)
print([cls.__name__for cls in D.])




 # isintstanc & issubclass
class Vehicle:
    pass
class Car(Vehicle):
    pass
class ElectricCar(Car):
    pass
tesla = ElectricCar()
print(isinstance(tesla, ElectricCar))
print(isinstance(tesla, Car))
print(isinstance(tesla, Vehicle))
print(isinstance(tesla, str))











# from abc import ABC, abstractmethod
# class shape (ABC):
#      def__init__(self, color):
#      self.color = color

#      @abstractmethod
#      def area(self):
#           pass
#      @abstractmethod
#      def area(self):  return 3.14159 * self.r**
#      def perimeter(self): return 2 * 3.14159