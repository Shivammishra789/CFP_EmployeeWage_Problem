'''Calculating daily employee wage '''
import random

WAGE_PER_HOUR = 20
FULL_DAY = 8
ABSENT = 0
# generating random number
rand_num = (random.randint(0, 1))
if rand_num == 1:
    emp_hrs = FULL_DAY
else:
    emp_hrs = ABSENT

daily_emp_wage = WAGE_PER_HOUR * emp_hrs
print('Daily employee wage is:', daily_emp_wage)