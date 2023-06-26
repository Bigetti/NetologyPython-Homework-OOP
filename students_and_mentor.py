class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_for_l(self, lecturer, course, grade):
        if isinstance(lecturer, Mentor) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rate_fr_st:
                lecturer.rate_fr_st[course] += [grade]
            else:
                lecturer.rate_fr_st[course] = [grade]
        else:
            return 'Mistake'
        
    def get_average_rate_hw(self):
        total_grades = 0  # Переменная для хранения общей суммы оценок
        total_count = 0  # Переменная для хранения общего количества оценок
        for rates_list in self.grades.values():  # Перебираем списки оценок в словаре
            total_grades += sum(rates_list)  # Добавляем сумму оценок в общую сумму
            total_count += len(rates_list)  # Увеличиваем общее количество оценок
        if total_count == 0:
            return 0  # Возвращаем 0, если нет оценок
        average_rate = total_grades / total_count  # Вычисляем среднюю оценку
        return average_rate


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_rate_hw()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res
        



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
        

    
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.courses_attached = []
        self.rate_fr_st = {}
       

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}'
        return res
    

    
        
    def get_average_grade(self):
        total_grades = 0  # Переменная для хранения общей суммы оценок
        total_count = 0  # Переменная для хранения общего количества оценок
        for grades_list in self.rate_fr_st.values():  # Перебираем списки оценок в словаре
            total_grades += sum(grades_list)  # Добавляем сумму оценок в общую сумму
            total_count += len(grades_list)  # Увеличиваем общее количество оценок
        if total_count == 0:
            return 0  # Возвращаем 0, если нет оценок
        average_grade = total_grades / total_count  # Вычисляем среднюю оценку
        return average_grade



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    #     # self.courses_attached = []
        

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Mistake'
        

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname},\nкурсы:{self.courses_attached}'
        return res
    
   
        
        

best_student = Student('Kos', 'Barbos', '23')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Bady')
cool_reviewer.courses_attached += ['Python']

my_lector = Lecturer('Another', 'One')
my_lector.courses_attached += ['Python']
best_student.rate_for_l(my_lector, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Python', 10)


print(best_student)
# print(best_student.grades)
# print(cool_reviewer)
# print(my_lector.rate_fr_st)
# print(my_lector)
