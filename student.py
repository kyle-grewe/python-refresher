#Defining what student is
class Student:
    def __init__(self, name, major, gpa):
        self.name = name #Name of the Student object will = Name that we pass in
        self.major = major #Name of the Student major = Name of the major that we pass in
        self.gpa = gpa
        

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


    def add_to_list(self):
        students = []
        major = []
        gpa = []
        return("Data saved successfully")