#Public Member
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("Name:",self.name,"Salary:",self.salary)
emp=Employee("Thanu",5600)
#print("Name:",emp.name,"Salary:",emp.salary)
emp.show()

#Private Member

class Staff:
    # constructor
    def __init__(self, count, wages):
        # public data member
        self.count = count
        # private member
        self.__wages = wages

    def show(self):
        # private members are accessible from a class
        print("Count: ", self.count, 'Wages:', self.__wages)

# creating object of a class
stf = Staff(12, 10000)
stf.show()


#Protected Member

class Branch:
    def __init__(self):
        self._project="Customer Segmentation"
class Students(Branch):
    def __init__(self,name):
        self.name=name
        Branch.__init__(self)
    def show(self):
        print("Branch name :", self.name)
        print("Working on project :", self._project)
s=Students("EEE")
s.show()
print("project:",s._project)
