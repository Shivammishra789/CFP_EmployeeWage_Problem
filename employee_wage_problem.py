'''Calculating daily employee wage for full time, part time or absent '''
import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
ABSENT = 0
emp_hrs = 0

# generating random number
rand_num = (random.randint(0, 2))
print(rand_num)
if rand_num == 1:
    emp_hrs = FULL_TIME
elif rand_num == 2:
    emp_hrs = PART_TIME
else:
    emp_hrs = ABSENT

daily_emp_wage = WAGE_PER_HOUR * emp_hrs
print('Daily employee wage is:', daily_emp_wage)