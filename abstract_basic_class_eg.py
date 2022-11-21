"""A BASIC EXAMPLE FOR UNDERSTANDING ABSTRACT CLASSES"""

from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self, a):
        self.__a = a
    
    @abstractmethod
    def __str__(self):
        return f"{self.__a}"
    
    def get_value(self):
        return "Yes! I'm coming"

class B(A):
    def __init__(self, a):
        super().__init__(a)
    
    def __str__(self):
        return super().__str__()

if __name__ == "__main__":
    b = B(2)
    print(b)
    print(b.get_value())