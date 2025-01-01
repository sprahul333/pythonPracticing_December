class Emp:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def showEmpDetails(self):
        print(f'Welcome {self.name} to the Company')

class QA(Emp):

    def __init__(self, name, phone, role, package):
        super().__init__(name, phone)  # Calling the parent class constructor (need not be in the first line)
        self.role = role
        self.package = package

    def showEmpDetails(self):
        super().showEmpDetails()
        print(f'\tYour role is {self.role} and your package is {self.package}')


qa1 = QA("Umesh", 1234567890, "SDET", 100000)
qa1.showEmpDetails()

qa2 = QA("Selenium", 835894333, "SDET", 200000)
qa2.showEmpDetails()

qa3 = QA("Python", 9876538923, "SDET", 300000)
qa3.showEmpDetails()
