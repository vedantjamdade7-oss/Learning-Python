# Four features in OOPs
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism


# Abstraction
# Hiding unnecesary deatils from users through class, methods

# class - blueprint or template
class student:
    def __init__(self,name,grade,idcard_no,percentage): # method
        self.name = name # Attribute
        self.grade = grade # Attribute
        self.idcard_no = idcard_no
        self.percentage = percentage 

    def student_details(self): #method - Abstraction
        print(f"{self.name} is in class {self.grade} and has {self.percentage+1} % ")# hidden from users

    def student_idcard(self):
        print(f"student name {self.name} class {self.grade} idcard number {self.idcard}")

# object - instance of class
student1 = student('vedant',11,111,89)
# print(student1.name, student1.grade)

student2 = student('falguni',12,121,94)
# print(student2.name, student2.grade)

student1.student_details()
# student2.student_details()

# student1.student_idcard()
# student2.student_idcard()
