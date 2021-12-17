'''Computing employee wage for multiple companies which are having their own wage,
 number of working days and working hours per month'''
import random


class EmployeeWage:

    FULL_TIME = 8
    PART_TIME = 4
    ABSENT = 0

    # passing parameters to function
    def calculate_employee_wage(self, company, wage_per_hour, monthly_working_days, max_hours_per_month):
        """" Calculating employee wage with parameters passed"""
        monthly_emp_wage = 0
        emp_working_days = 0
        emp_working_hrs = 0

        # loop runs till monthly working days 20 or monthly working hrs 100 is reached
        while emp_working_days < monthly_working_days and emp_working_hrs <= max_hours_per_month:
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
            monthly_emp_wage = wage_per_hour * emp_working_hrs

        print('Total working hours:', emp_working_hrs)
        print('Monthly employee wage for company',company,"is", monthly_emp_wage)


# creating objects and passing values to method
employee1 = EmployeeWage()
employee1.calculate_employee_wage('Tata',20,20,100)
employee2 = EmployeeWage()
employee2.calculate_employee_wage('Sinclair',25,30,100)
