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
        return "name: {0}, gender: {1}, image_url: {2}".format(
            self.name, self.gender, self.image_url)


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


course_name = ["Mathematics", "Chemistry", "English", "Science",
               "Psychology", "Geology", "History", "Art & Design"]
classrooms = [401, 402, 403, 404, 405, 406, 407, 408]
teachers = ["Tom", "Susan", "Iris", "Isabel",
            "Jef", "Nick", "Martin", "Kathrin"]
grades = ["A", "A", "B", "B", "B", "B", "C", "C", "C", "C", "C", "C", "D", "D", "D", "D", "E", "E", "E", "Fx", "Fx", "F"]
male_names = ["Alan", "Steve", "Roger", "Georg", "Dwayne", "Michael"]
female_names = ["Michelle", "Brie", "Natascha", "Taylor", "Selena", "Sofia"]
gender = ["Male", "Female"]


def gen_students(n: int):
    for i in range(n):
        courses: Course = list()
        g = random.choice(gender)
        with open("./students.csv", "a") as f_obj:
            if g == "Male":
                gen_courses(courses)
                male = Student(random.choice(male_names), g,
                                DataSheet(courses), "img" + str(i) + ".jpg")
                for course in male.data_sheet.courses:
                    f_obj.write(
                        f"stud_name: {male.name}, course_name: {course.name}, teacher: {course.teacher}, ects: {course.ETCS}, classroom: {course.classroom}, grade: {course.grade}, img_url: {male.image_url}\n")
            else:
                gen_courses(courses)
                female = Student(
                    random.choice(female_names),
                    g,
                    DataSheet(courses),
                    "img" + str(i) + ".jpg")
                for course in female.data_sheet.courses:
                    f_obj.write(
                        f"stud_name: {female.name}, course_name: {course.name}, teacher: {course.teacher}, ects: {course.ETCS}, classroom: {course.classroom}, grade: {course.grade}, img_url: {female.image_url}\n")


def gen_courses(courses):
    new_course_names = course_name.copy()
    new_classroms = classrooms.copy()
    new_teachers = teachers.copy()
    for _ in range(5):
        courses.append(
            Course(
                new_course_names.pop(random.choice(range(len(new_course_names)))),
                new_classroms.pop(random.choice(range(len(new_classroms)))),
                new_teachers.pop(random.choice(range(len(new_teachers)))),
                20,
                random.choice(grades)))
        


gen_students(20)
