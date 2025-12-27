# Dunder Methods = means Double underscore Methods


class Point:
    def __init__(self, x_pos, y_pos, z_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        
    def __add__(self, other):
        new_x_pos = self.x_pos + other.x_pos
        new_y_pos = self.y_pos + other.y_pos
        new_z_pos = self.z_pos + other.z_pos
        
        return new_x_pos, new_y_pos, new_z_pos
    
    def __gt__(self, other):
        return (self.x_pos + self.y_pos + self.z_pos) > (other.x_pos + other.y_pos + other.z_pos)
    
    def __len__(self):
        return int((self.x_pos ** 2 + self.y_pos ** 2 + self.z_pos ** 2) ** 0.5)
    
    def __getitem__(self, index):
        if index == 0:
            return self.x_pos
        elif index == 1:
            return self.y_pos
        elif index == 2:
            return self.z_pos
        else:
            # return "Coordinate Index Out of Range"
            raise Exception
        


p1 = Point(2, 3, 4)
p2 = Point(5, 6, 7)

# print(p1 + p2)
# print(p1 > p2)
# print(len(p1))

# print(p1[0])

from abc import ABC, abstractmethod


class Person(ABC):
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person Constructor called")
        
    @abstractmethod
    def print_role(self):
        pass
    
class Student(Person):
    
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.sd_courses_list = []
    
    def print_role(self):
        return "Student"
    
    def enroll_to_course(self, course_name):
        self.sd_courses_list.append(course_name)
        
    def show_enrolled_courses(self):
        print(self.sd_courses_list)
    
    def __str__(self):
        # return str(self.student_id)
        return f"{self.student_id}, {self.name}, {self.age}"
    
    
std1 = Student(1, "Nani", 21)
print(std1)
std1.enroll_to_course("DBMS")
std1.enroll_to_course("OPPS")
std1.enroll_to_course("OS")
std1.show_enrolled_courses()