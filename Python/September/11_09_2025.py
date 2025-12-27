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
        # return str(self.student_id, self.name, self.age)
        return f"{self.student_id}, {self.name}, {self.age}"
    
class Teacher(Person):
    
    def __init__(self, teacher_id, name, age):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.te_assigned_courses_list = []
        
    def print_role(self):
        return "Teacher"
    def assign_to_course(self,course_name):
        self.te_assigned_courses_list.append(course_name)
    
    def show_assign_courses(self):
        print(self.te_assigned_courses_list)
        
    def __str__(self):
        return f"{self.teacher_id}, {self.name}, {self.age}"
    
class Course():
    
    def __init__(self, course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students_name_list = []
        
    def assign_sd_to_course(self, student_name):
        self.students_name_list.append(student_name)
        
    def show_enrolled_students_name_list(self):
        print(self.students_name_list)
        
    def __str__(self):
        return f"{self.course_name}, {self.course_code}, {self.teacher}"

class Department():
    
    def __init__(self, department_name):
        self.department_name = department_name
        self.department_courses_list = []
        self.department_teachers_list = []
        self.department_students_list = []
    
    def courses_in_department(self, course_name):
        self.department_courses_list.append(course_name)
        
    def teachers_in_department(self, teacher_name):
        self.department_teachers_list.append(teacher_name)
        
    def students_in_department(self, student_name):
        self.department_students_list.append(student_name)

    def Provide_Summary_info(self):
        print(self.department_name)
        print(self.department_courses_list)
        print(self.department_teachers_list)
        print(self.department_students_list)
    
    def __str__(self):
        return f"{self.department_name}"
    
class Administration():
    
    def __init__(self):
        self.list_of_department_names = []
        
    def add_departments(self, department_names):
        self.list_of_department_names.append(department_names)
    
    def Provide_Department_info(self):
        print(self.list_of_department_names)


std1 = Student(1, "Nani", 21)
std2 = Teacher(2, "Tharun", 35)
cou1 = Course("Python", "PY001", "Ram")
dep1 = Department("CSE")
adm1 = Administration()


print(std1)
std1.enroll_to_course("DBMS")
std1.enroll_to_course("OPPS")
std1.enroll_to_course("OS")
std1.show_enrolled_courses()

print(std2)
std2.assign_to_course("Python")
std2.assign_to_course("HTML")
std2.assign_to_course("CSS")
std2.show_assign_courses()

print(cou1)
cou1.assign_sd_to_course("Nani")
cou1.assign_sd_to_course("Tharun")
cou1.assign_sd_to_course("Ramanji")
cou1.show_enrolled_students_name_list()

print(dep1)
dep1.courses_in_department("Python")
dep1.courses_in_department("Java")
dep1.teachers_in_department("Tharun")
dep1.teachers_in_department("Venkat")
dep1.students_in_department("Nani")
dep1.students_in_department("Sai")
dep1.Provide_Summary_info()

adm1.add_departments("CSE")
adm1.add_departments("EEE")
adm1.add_departments("ECE")
adm1.Provide_Department_info()