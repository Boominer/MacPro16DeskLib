# Python statis method
"""
  1. belong to the class, not the instance. 
  2. Does not use self or cls 
  3. behaves like a normal function, but is namespaced inside the class
"""
class Utils:
    @statismethod
    def add(a, b):
        return a+b

print(Utils.add(1,3)) # 7 

# abstract method 
"""
    1. it must be defined inside the class that inherit from.
    2. if a subclass does not implement the abstract method, you can not instantiate it
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 

class circle(Shape):
    def area(self):
        return 3.14 * r * r 