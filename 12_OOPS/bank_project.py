# Bank System 

class Employee:
    def __init__(self,employee_id,employee_name,department,basic_salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.department=department
        self.__basic_salary=basic_salary

    def display_details(self):
        print("========== EMPLOYEE DETAILS =============")
        print("Employee ID :: ",self.employee_id)
        print("Employee NAme :: ",self.employee_name)
        print("Employee Department :: ",self.department)
        print("Employee Basic Salary :: ",self.__basic_salary)


    def get_basic_salary(self):
        return self.__basic_salary

    def update_salary(self,percentage):
        increment=self.__basic_salary*percentage/100
        self.__basic_salary+=increment
        print("Salary Updated Successfully ")
        print("New Salary :: ",self.__basic_salary)

    def calculate_salary(self):
        return self.__basic_salary

    def employee_types(self):
        return "Employee"



class FullTimeEmployee(Employee):
    def __init__(self, employee_id, employee_name, department, basic_salary,bonus,pf_percentage):
        super().__init__(employee_id, employee_name, department, basic_salary)
        self.bonus=bonus
        self.pf_percentage=pf_percentage

    def calculate_salary(self):
        pf=self.get_basic_salary()*self.pf_percentage/100
        net_salary=self.get_basic_salary()+self.bonus-pf
        return net_salary

    def employee_types(self):
        return "Full Time Employee" 

    def give_bonus(self,amount):
        self.bonus+=amount
        print("Bonus Added Successfully ")
        print("Updated Bnous :: ",self.bonus)


    def display_details(self):
        super().display_details()
        print("Employee Type :: ",self.employee_types())
        print("Bonus :: ",self.bonus)
        print("PF Percentage :: ",self.pf_percentage, "%")
        print("Net Salary :: ",self.calculate_salary())


class PartTimeEmployees(Employee):
    def __init__(self, employee_id, employee_name, department,hours_worked,hourly_rate):
        super().__init__(employee_id, employee_name, department, 0)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked

    def employee_types(self):
        return " Part Time EMployee "

    def display_details(self):
        print("EMployee ID :: ",self.employee_id)
        print("Employee NAme :: ",self.employee_name)
        print("Department Name :: ",self.department)
        print("EMployee Type :: ",self.employee_types())
        print("Total Hours worked :: ",self.hours_worked)
        print("Hourly Rate :: ",self.hourly_rate)
        print("Total Salary :: ",self.calculate_salary())


# create objects
emp1=FullTimeEmployee(101,"Ram","IT",40000,5000,12)
emp2=FullTimeEmployee(102,"Raj","CS",80000,6000,10)
emp3=PartTimeEmployees(103,"Rahul","Finanace",120,300)
emp4=PartTimeEmployees(104,"Priya","HR",150,400)

# store this objects in list 
employees=[emp1,emp2,emp3,emp4]

# print all employee details
print("\n ============ EMPLOYEE PAYROLL SYSTEM ===============")
for employee in employees:
    print("\n -----------------------------------------")
    employee.display_details()


# calculate salary

total_salary=0

for employee in employees:
    total_salary+=employee.calculate_salary()

print("Total Monthly Salary :: ",total_salary)


# find Emp with highest salary 
highest_paid=employees[0]

for employee in employees:
    if employee.calculate_salary()>highest_paid.calculate_salary():
        highest_paid=employee

print("\n\n Highest Paid EMployee :: ",highest_paid.employee_name)
print("Salary is ::",highest_paid.calculate_salary())

# count full time and part time employee  count
full_time_count=0
part_time_count=0

for employee in employees:
    if isinstance(employee,FullTimeEmployee):
        full_time_count+=1
    else:
        part_time_count+=1

print("\n Full Time EMployee Count :: ",full_time_count)
print("\n Part Time EMployee Count :: ",part_time_count)


# lowest paid employee 
# find employee working in IT Department 