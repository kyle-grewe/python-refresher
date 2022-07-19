#Defining what student is
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name #Name of the Student object will = Name that we pass in
        self.major = major #Name of the Student major = Name of the major that we pass in
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


