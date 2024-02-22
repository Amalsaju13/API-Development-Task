class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Employee Details: Name - {self.name}, ID - {self.emp_id}, Title - {self.title}, Department - {self.department}")

    def __str__(self):
        return f"{self.name} - ID: {self.emp_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        del self.departments[department_name]

    def display_departments(self):
        print("Departments in the company:")
        for department_name, department in self.departments.items():
            print(department_name)

def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display All Departments")
    print("7. Exit")

# Sample usage:
if __name__ == "__main__":
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")

            employee = Employee(name, emp_id, title, department)
            if department not in company.departments:
                print("Error: Department does not exist. Please add the department first.")
            else:
                company.departments[department].add_employee(employee)

        elif choice == "2":
            emp_id = input("Enter employee ID to remove: ")
            for department in company.departments.values():
                department.remove_employee(emp_id)

        elif choice == "3":
            department_name = input("Enter department name to display: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Error: Department not found.")

        elif choice == "4":
            department_name = input("Enter department name to add: ")
            department = Department(department_name)
            company.add_department(department)

        elif choice == "5":
            department_name = input("Enter department name to remove: ")
            if department_name in company.departments:
                company.remove_department(department_name)
            else:
                print("Error: Department not found.")

        elif choice == "6":
            company.display_departments()

        elif choice == "7":
            print("Exiting Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
