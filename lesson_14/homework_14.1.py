class Student:

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_score = 0

    def set_average_score(self, average_score):
        self.average_score = average_score

    def print_user_data(self):
        print(f'First name: {self.first_name}\nSecond name: {self.second_name}\n'
              f'Age: {self.age}\naverage score: {self.average_score}')


Taras_Bulba = Student(first_name='Taras', second_name='Bulba', age=55)
Taras_Bulba.set_average_score(average_score=4.5)

Taras_Bulba.print_user_data()


