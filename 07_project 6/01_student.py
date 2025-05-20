class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"this student name is {self.name} and its marks is {self.marks}"
    
obj1= Student("ali" , 98)
print(obj1.display())