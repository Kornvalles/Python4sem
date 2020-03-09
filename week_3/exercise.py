import random
import string

class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(grades):
        count = 0
        for grade in grades:
            count += grade
        return count / len(grades)
    
    def __str__(self):
        return "name: {0}, gender: {1}, image_url: {2}".format(self.name, self.gender, self.image_url)


class DataSheet():

    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list():
        return
    
    def __str__(self):
        return self.courses

class Course():
    
    def __init__(self, name, classroom, teacher, ETCS, grade=00):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

math = Course("Math", 402, "Ellen", 10, 12)
chem = Course("Chemistry", 403, "Bo", 10, 7)

male_names = ["Alan", "Steve", "Roger", "Georg", "Dwayne", "Michael"]
female_names = ["Michelle", "Brie", "Natascha", "Taylor", "Ellen", "Sofia"]
gender = ["Male", "Female"]
courses = [math, chem]

def gen_students(n):
    students: Student = list()
    for i in range(n):
        students.append(Student(names[i], random.choice(gender), DataSheet(courses), "img"+str(i)+".jpg"))
    return students

for s in gen_students(3):
    print(s)