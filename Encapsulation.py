class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)
    def work(self):
        print(self.name, 'is working on', self.project)
# creating object of a class
emp = Employee('Thanu', 8000, 'Cognine')
# calling public method of the class
emp.show()
emp.work()
