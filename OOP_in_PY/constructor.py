
# class Student:

#     name = "Mithila"
#     print("Adding new Student...")

# s1 = Student()
# print(s1.name)

# with constructor

class Student:

    def __init__(self, name, marks):

       self.name = name
       self.marks = marks
       print("Adding new Student...")

s1 = Student("Pakhi", 24.5)
print(s1.name, s1.marks)

s2 = Student("Pakhi1", 12)
print(s2.name, s2.marks)