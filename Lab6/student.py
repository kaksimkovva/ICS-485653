class Student:
    grade = {
        'max_exam_grade': 100,
        'max_laboratory_grade': 5,
        'number_of_laboratory_works': 10,
        'scores_for_automatic_evaluation': 0.6,
    }

    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def exam_attempts(self, attempts: int, last_grade: float):
        print(f'Attempts: {attempts}\n Last grade:{last_grade}')

    def individual_attempts(self, attempts: int, last_grade: float):
        print(f'Attempts: {attempts}\n Last grade:{last_grade}')


student = Student("Vasia", 4)
student.exam_attempts(5, 4)
student.individual_attempts(4, 4)