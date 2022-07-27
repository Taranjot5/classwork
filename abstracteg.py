from abc import ABC,abstractmethod
class student(ABC):
    @abstractmethod
    def f1(self):
        pass
class test(student):
    def f1(self):
        print("f1")
obj=test()
obj.f1()
