# OOPs - object oriented programming

# using OOPs - creating student records

# class - blueprint or template
# __init__ method - constructor, value initilize-fix
class student:
    def __init__(self,name,grade,idcard_no,percentage,team): # method
        self.name = name # Attribute
        self.grade = grade # Attribute
        self.idcard_no = idcard_no
        self.percentage = percentage
        self.team = team

    def student_details(self): #method
        print(f"{self.name} is in class {self.grade} and has {self.percentage} % ")

    def student_idcard(self):
        print(f"student name {self.name} class {self.grade} idcard number {self.idcard}")

team1 = 'A'
team2 = 'B'

# object - instance of class
student1 = student('vedant',11,111,89,'A')
# print(student1.name, student1.grade)

student2 = student('falguni',12,121,94,'B')
# print(student2.name, student2.grade)

# student1.student_details()
# student2.student_details()

# student1.student_idcard()
# student2.student_idcard()

print(student1.__dict__)

# modify object property
print(student1.percentage) # old percent
student1.percentage = 98 # modify 
print(student1.percentage) # get new percent

print(student1.grade) # old 
student1.grade = 12 # modify 
print(student1.grade) # get new

#  delete object propert
print(student2.__dict__)
del student2.percentage
print(student2.__dict__)

# delete object
del student1
print(student1)
