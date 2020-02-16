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


class DataSheet():

    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list():


class Course():

    def __init__(self, name, classroom, teacher, ETCS, grade=00):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade
