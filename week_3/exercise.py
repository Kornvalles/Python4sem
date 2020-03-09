import random
import string

class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self, grades):
        count = 0
        for grade in grades:
            count += grade
        return count / len(grades)
    
    def __str__(self):
        return "name: {0}, gender: {1}, image_url: {2}".format(self.name, self.gender, self.image_url)


class DataSheet():

    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list(self):
        courses: Course = list()
        for course in self.courses:
            courses.append(course.grade)
        return courses
    
    def __str__(self):
        return self.courses

class Course():
    
    def __init__(self, name, classroom, teacher, ETCS, grade=00):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

course_name = ["Mathematics", "Chemistry", "English", "Science", "Psychology", "Geology", "History", "Art & Design"]
classrooms = [401, 402, 403, 404, 405, 406, 407, 408]
teachers = ["Tom", "Susan", "Iris", "Isabel", "Jef", "Nick", "Martin", "Kathrin"]
ETCSs = [20, 40, 60]
grades = ["A", "B", "C", "D", "E", "Fx", "F"]
male_names = ["Alan", "Steve", "Roger", "Georg", "Dwayne", "Michael"]
female_names = ["Michelle", "Brie", "Natascha", "Taylor", "Selena", "Sofia"]
gender = ["Male", "Female"]


def gen_students(n: int):
    students: Student = list()
    courses: Course = list()
    for i in range(n):
        g = random.choice(gender)
        with open("./students.csv", "a") as f_obj:
            if g == "Male":
                for j in range(0,4):
                    courses.append(Course(random.choice(course_name), random.choice(classrooms), random.choice(teachers), random.choice(ETCSs), random.choice(grades)))
                male = Student(random.choice(male_names), g, DataSheet(courses), "img"+str(i)+".jpg")
                for course in male.data_sheet.courses:
                    f_obj.write("stud_name: {0}, course_name: {1}, teacher: {2}, ects: {3}, classroom: {4}, grade: {5}, img_url: {6}\n".format(male.name, course.name, course.teacher, course.ETCS, course.classroom, course.grade, male.image_url))
            else:
                for j in range(0,4):
                    courses.append(Course(random.choice(course_name), random.choice(classrooms), random.choice(teachers), random.choice(ETCSs), random.choice(grades)))
                female = Student(random.choice(female_names), g, DataSheet(courses), "img"+str(i)+".jpg")
                for course in female.data_sheet.courses:
                    f_obj.write("stud_name: {0}, course_name: {1}, teacher: {2}, ects: {3}, classroom: {4}, grade: {5}, img_url: {6}\n".format(female.name, course.name, course.teacher, course.ETCS, course.classroom, course.grade, female.image_url))
    return students

gen_students(20)
