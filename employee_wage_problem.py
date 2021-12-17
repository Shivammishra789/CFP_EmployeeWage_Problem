'''Computing employee wage for multiple companies which are having their own wage,
 number of working days and working hours per month'''
import random


class EmployeeWage:

    # static variables
    FULL_TIME = 8
    PART_TIME = 4
    ABSENT = 0

    def __init__(self, *params):
        # initializing values to instance variables
        self.company = params[0]
        self.wage_per_hour = params[1]
        self.monthly_working_days = params[2]
        self.max_hours_per_month = params[3]

    def calculate_employee_wage(self):
        """" Calculating employee wage """
        monthly_emp_wage = 0
        emp_working_days = 0
        emp_working_hrs = 0

        # loop runs till monthly working days 20 or monthly working hrs 100 is reached
        while emp_working_days < self.monthly_working_days and emp_working_hrs <= self.max_hours_per_month:
            emp_working_days += 1

            # generating random number
            rand_num = (random.randint(0, 2))
            if rand_num == 1:
                emp_hrs = self.FULL_TIME
            elif rand_num == 2:
                emp_hrs = self.PART_TIME
            else:
                emp_hrs = self.ABSENT
            emp_working_hrs += emp_hrs

            # loop will exit if hrs are greater than 100
            if emp_working_hrs > 100:
                emp_working_hrs -= emp_hrs
                break
            self.monthly_emp_wage = self.wage_per_hour * emp_working_hrs

    def __str__(self):
        return "(Company Name: "+self.company +", Monthly Salary: "+ str(self.monthly_emp_wage)+")"


# creating object
employee1 = EmployeeWage('Tata',20,20,100)
employee1.calculate_employee_wage()
print(employee1)
employee2 = EmployeeWage('Sinclair',25,30,100)
employee2.calculate_employee_wage()
print(employee2)