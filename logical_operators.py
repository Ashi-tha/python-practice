#logical operators = evaluate multiple conditions(or,and,not)
#             or  = atleast one condition must be true
#             and = both conditions must be true
#             not = inverts the condition(not false,not true)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")


