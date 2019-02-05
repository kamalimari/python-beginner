class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)

    def display(self):
        print("I am ", self.name)
        print("I am", self.age)


class Student(Person):

    def islearner(self):
        print("True")


p = Person("kamali", 54)
print(p.display())

stu = Student("deepika", 24)
print(stu.display(), stu.islearner())



