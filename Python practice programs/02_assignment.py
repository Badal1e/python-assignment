from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass

class Male:
    def get_gender(self):
        print("Male")

class Female:
    def get_gender(self):
        print("Female")

m = Male()
f = Female()

m.get_gender()