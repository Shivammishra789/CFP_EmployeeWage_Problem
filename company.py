'''
@author: Shivam Mishra
@date: 22-12-21 11:41 AM
@desc: Contains company class and functions to get employee wage details
'''


class Company:
    """initializing values to instance variables company, wage_per_hour, monthly_working_days, max_hours_per_month"""
    employee_wage_details = []

    def __init__(self, company, wage_per_hour, monthly_working_days, max_hours_per_month):
        self.company = company
        self.wage_per_hour = wage_per_hour
        self.monthly_working_days = monthly_working_days
        self.max_hours_per_month = max_hours_per_month

    def store_employee_wage_details(self, employee_obj):
        '''Adding employee wage details to list'''
        self.employee_wage_details.append(employee_obj)

    @classmethod
    def display_employee_wage_details(cls):
        '''Displays employee wage details'''
        for i in range(len(cls.employee_wage_details)):
            print(cls.employee_wage_details[i])

    @classmethod
    def query_salary_by_company_name(cls):
        '''Gives salary of employee when quered by company name'''
        company_name = input("enter the company name : ")
        for i in range(len(cls.employee_wage_details)):
            if company_name.lower() == cls.employee_wage_details[i].company:
                print("Monthly salary : " + str(cls.employee_wage_details[i].monthly_emp_wage))
                break
        else:
            print("Entered company name not found")

