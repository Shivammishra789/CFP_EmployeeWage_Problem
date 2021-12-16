'''Calculating monthly employee wage for full time, part time or absent for 20 days'''
import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
ABSENT = 0
emp_hrs = 0
monthly_emp_wage = 0


def random_employee_presentee():
    global emp_hrs
    # generating random number
    rand_num = (random.randint(0, 2))
    if rand_num == 1:
        emp_hrs = FULL_TIME
    elif rand_num == 2:
        emp_hrs = PART_TIME
    else:
        emp_hrs = ABSENT


# getting random employee presentee for 20 days
for x in range(0, 20):
    # calling function
    random_employee_presentee()
    daily_emp_wage = WAGE_PER_HOUR * emp_hrs
    monthly_emp_wage += daily_emp_wage
print('Monthly employee wage is:', monthly_emp_wage)