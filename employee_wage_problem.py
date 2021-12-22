'''
@author: Shivam Mishra
@date: 22-12-21 11:41 AM
@desc: Employee wage is calculated
'''

import random
from company import Company

class EmployeeWage(Company):
    '''
    Computing and storing daily and monthly employee wage for multiple companies which are having their own wage,
    number of working days and working hours per month
    '''

    # static variables
    FULL_TIME = 8
    PART_TIME = 4
    ABSENT = 0

    def employee_work_hrs(self):
        """ Generating random work hours full time-8, part time-4 or absent-0"""
        # generating random number
        rand_num = (random.randint(0, 2))
        if rand_num == 1:
            self.emp_hrs = self.FULL_TIME
        elif rand_num == 2:
            self.emp_hrs = self.PART_TIME
        else:
            self.emp_hrs = self.ABSENT

    def calculate_employee_wage(self,emp_obj):
        """ Calculating employee wage"""
        emp_working_days = 0
        emp_working_hrs = 0

        self.daily_wage_list = []

        # loop runs till monthly working days  or monthly working hrs is reached
        while emp_working_days < self.monthly_working_days and emp_working_hrs <= self.max_hours_per_month:
            emp_working_days += 1
            self.employee_work_hrs()
            emp_working_hrs += self.emp_hrs

            # loop will exit if hrs are greater than 100
            if emp_working_hrs > 100:
                emp_working_hrs -= self.emp_hrs
                break
            daily_wage = self.wage_per_hour * self.emp_hrs
            # storing daily wage in list
            self.daily_wage_list.append(daily_wage)
        self.monthly_emp_wage = self.wage_per_hour * emp_working_hrs

        self.store_employee_wage_details(emp_obj)

    def __str__(self):
        return "(Company Name: "+self.company + ", DailyWage:" + str(self.daily_wage_list) + ", Monthly Salary: " + str(self.monthly_emp_wage)+")"

# creating object
employee1 = EmployeeWage('tata',20,20,100)
employee1.calculate_employee_wage(employee1)
employee2 = EmployeeWage('sinclair',25,30,100)
employee2.calculate_employee_wage(employee2)

Company.display_employee_wage_details()
Company.query_salary_by_company_name()


