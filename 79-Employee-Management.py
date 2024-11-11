class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = None
        self.projects = []

    def assign_department(self, department):
        self.department = department

    def add_project(self, project):
        self.projects.append(project)

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        if self.department:
            print(f"Department: {self.department.name}")
        print("Projects:", ", ".join([p.name for p in self.projects]) if self.projects else "No projects assigned")


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.assign_department(self)

    def list_employees(self):
        print(f"Employees in {self.name} Department:")
        for emp in self.employees:
            print(f" - {emp.name} (ID: {emp.emp_id}, Position: {emp.position})")


class Project:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.employees = []

    def assign_employee(self, employee):
        self.employees.append(employee)
        employee.add_project(self)

    def show_project_details(self):
        print(f"Project Name: {self.name}")
        print(f"Deadline: {self.deadline}")
        print("Assigned Employees:")
        for emp in self.employees:
            print(f" - {emp.name} (ID: {emp.emp_id})")


dept = Department("IT")
emp1 = Employee(1, "Talha", "Developer")
emp2 = Employee(2, "Ab", "Analyst")

dept.add_employee(emp1)
dept.add_employee(emp2)

proj1 = Project("AI Development", "2025-01-15")
proj1.assign_employee(emp1)

emp1.display_info()
print("\n")
dept.list_employees()
print("\n")
proj1.show_project_details()
