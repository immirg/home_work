class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __setattr__(self, key, value):
        if key in ['name', 'departament', 'programming_language']:
            if len(value.strip()) <= 0:
                raise ValueError(f'Введено не корректно значение для {key}')
        if key in ['salary', 'team_size']:
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f'Введен не корректный размер для {key}')
        super().__setattr__(key, value)


class Manager(Employee):
    def __init__(self, name, departament, salary):
        Employee.__init__(self, name, salary)
        self.departament = departament


class Developer(Employee):
    def __init__(self, name, programming_language, salary):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, team_size, departament, programming_language, salary):
        Manager.__init__(self, name, departament, salary)
        Developer.__init__(self, name, programming_language, salary)
        self.team_size = team_size


alan = TeamLead(name='Alan', team_size=7, departament='AQA', programming_language='python', salary=4000)
print(alan.name, alan.team_size, alan.departament, alan.programming_language, alan.salary)

