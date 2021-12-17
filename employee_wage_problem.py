'''Refactored the Code to write a Class Method to Compute Employee wage
   (Class method and class variables used)'''
import random


class EmployeeWage:
    WAGE_PER_HOUR = 20
    MONTHLY_WORKING_DAYS = 20
    MONTHLY_WORKING_HRS = 100
    FULL_TIME = 8
    PART_TIME = 4
    ABSENT = 0


    def calculate_employee_wage(self):
        """" Calculating employee wage """
        monthly_emp_wage = 0
        emp_working_days = 0
        emp_working_hrs = 0
        # loop runs till monthly working days 20 or monthly working hrs 100 is reached
        while emp_working_days < self.MONTHLY_WORKING_DAYS and emp_working_hrs <= self.MONTHLY_WORKING_HRS:
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
            print('Day:', emp_working_days, 'Hrs Present:', emp_hrs)
            monthly_emp_wage = self.WAGE_PER_HOUR * emp_working_hrs

        print('Total working hours:', emp_working_hrs)
        print('Monthly employee wage is:', monthly_emp_wage)

employee = EmployeeWage()
employee.calculate_employee_wage()