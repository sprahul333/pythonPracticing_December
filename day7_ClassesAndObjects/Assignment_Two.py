class Employee:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Department: {self.department}')


empName=input("Enter the Employee Name ('or done to finish')")

while empName.lower()!='done':
    empAge=int(input("Enter the Employee Age"))
    empDepartment=input("Enter the Employee Department")

    emp1=Employee(empName,empAge,empDepartment)
    emp1.display()

    empName = input("Enter the Employee Name ('or done to finish')")

