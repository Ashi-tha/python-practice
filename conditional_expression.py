#conditional expression (ternary operator): A one-line shortcut for the if - else statements
#                                          print or assign one or two values based on a condition
#                                          x if condition else y

num = int(input("enter a number"))
print("positive" if num>0 else "negative")


age = int(input("enter your age " ))
print("eligible" if age >18 else "you are not eligible")


num1 = int(input("enter a number"))
result = "even" if num1%2==0 else "odd"
print(result)