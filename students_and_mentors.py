class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        return 'Ошибка'

    def __average_grade(self):
        sum_student_grades = sum(map(sum, self.grades.values()))
        len_student_grades = sum(map(len, self.grades.values()))
        return (sum_student_grades / len_student_grades)

    def __list_grades(self):
        return list(self.grades.keys())

    def __str__(self):
        student_print = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнии задания: {self.__average_grade()}\nКурсы в процессе изучения: {", ".join(self.__list_grades())}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return student_print

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def __average_grade(self):
        sum_lecturer_grades = sum(map(sum, self.grades.values()))
        len_lecturer_grades = sum(map(len, self.grades.values()))
        return (sum_lecturer_grades / len_lecturer_grades)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.__average_grade() > other.__average_grade():
                return f'У {self.name} {self.surname} средняя оценка лучше, чем у {other.name} {other.surname}.'
            elif self.__average_grade() < other.__average_grade():
                return f'У {other.name} {other.surname} средняя оценка лучше, чем у {self.name} {self.surname}.'
            else:
                return f'У {other.name} {other.surname} и {self.name} {self.surname} одинаковая средняя оценка.'
        else:
            return 'Ошибка'

    def __str__(self):
        lecturer_print = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}'
        return lecturer_print

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        return 'Ошибка'

    def __str__(self):
        reviewer_print = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer_print

student_one = Student('Denis', 'Khaidarov', 'Male')
student_one.courses_in_progress += ['Python']
student_one.courses_in_progress += ['Git']
student_one.finished_courses += ['Введение в программирование']

student_two = Student('Sergey', 'Korolkov', 'Male')
student_two.courses_in_progress += ['Python']
student_two.courses_in_progress += ['Git']
student_two.finished_courses += ['Введение в программирование']

reviewer_one = Reviewer('Eduard', 'Pascal')
reviewer_one.courses_attached += ['Python']
reviewer_one.courses_attached += ['Git']

reviewer_two = Reviewer('Eduard', 'Pascal')
reviewer_two.courses_attached += ['Python']
reviewer_two.courses_attached += ['Git']

lecturer_one = Lecturer('Sergey', 'Svetlakov')
lecturer_one.courses_attached += ['Python']
lecturer_one.courses_attached += ['Git']

lecturer_two = Lecturer('Semen', 'Slepakov')
lecturer_two.courses_attached += ['Python']
lecturer_two.courses_attached += ['Git']

student_one.rate_lecturer(lecturer_one, 'Python', 10)
student_one.rate_lecturer(lecturer_one, 'Python', 9)
student_one.rate_lecturer(lecturer_one, 'Python', 8)
student_one.rate_lecturer(lecturer_one, 'Git', 10)
student_one.rate_lecturer(lecturer_one, 'Git', 9)
student_one.rate_lecturer(lecturer_one, 'Git', 8)

student_two.rate_lecturer(lecturer_two, 'Python', 8)
student_two.rate_lecturer(lecturer_two, 'Python', 7)
student_two.rate_lecturer(lecturer_two, 'Python', 6)
student_two.rate_lecturer(lecturer_two, 'Git', 6)
student_two.rate_lecturer(lecturer_two, 'Git', 5)
student_two.rate_lecturer(lecturer_two, 'Git', 4)

reviewer_one.rate_student(student_one, 'Python', 9)
reviewer_one.rate_student(student_one, 'Python', 8)
reviewer_one.rate_student(student_one, 'Python', 7)
reviewer_one.rate_student(student_one, 'Git', 5)
reviewer_one.rate_student(student_one, 'Git', 4)
reviewer_one.rate_student(student_one, 'Git',3)

reviewer_two.rate_student(student_two, 'Python', 9)
reviewer_two.rate_student(student_two, 'Python', 8)
reviewer_two.rate_student(student_two, 'Python', 7)
reviewer_two.rate_student(student_two, 'Git', 9)
reviewer_two.rate_student(student_two, 'Git', 8)
reviewer_two.rate_student(student_two, 'Git', 7)

all_students = [student_one, student_two]

def average_student_grade(student, course):
    grade_list = []
    for student in all_students:
        if course in student.grades:
            grade_list += student.grades[course]
        else:
            return 'Ошибка'
        result = sum(grade_list) / len(grade_list)
    return result

all_lecturers = [lecturer_one, lecturer_two]

def average_lecturer_grade(lecturer, course):
    list_grade = []
    for lecturer in all_lecturers:
        if course in lecturer.grades:
            list_grade += lecturer.grades[course]
        else:
            return 'Ошибка'
        result = sum(list_grade) / len(list_grade)
    return result

print('')
print(reviewer_one)
print('')
print(lecturer_one)
print('')
print(lecturer_two)
print('')
print(student_one)
print('')
print(lecturer_one.__lt__(lecturer_two))
print('')
print(f"Средняя оценка студентов по курсу Python: {average_student_grade(all_students, 'Python')}")
print('')
print(f"Средняя оценка студентов по курсу Git: {average_student_grade(all_students, 'Git')}")
print('')
print(f"Средняя оценка лекторов по курсу Python: {average_lecturer_grade(all_lecturers, 'Python')}")
print('')
print(f"Средняя оценка лекторов по курсу Git: {average_lecturer_grade(all_lecturers, 'Git')}")