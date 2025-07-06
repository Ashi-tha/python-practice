#python calcularor

operator = input("enter an operator(+ - * / %): ")
if operator not in ["+","-","*","/","%"]:
    print(f"{operator} is not a valid input")
else:    
    num1 = float(input("enter the 1st number: "))
    num2 = float(input("enter the 2nd number: "))

result = None
if operator == "+" :
    result = num1+num2
    
elif operator == "-":
    result = num1-num2
    
elif operator == "*":
    result = num1*num2
    
elif operator == "/":
      if num2!=0:
          result = num1/num2
      else:
          print("error : cannot divide by zero")
    
elif operator == "%":
    if num2!=0:
         result = num1%num2
    else:
        print("error : cannot do modulus by 0")

if result is not None:
    print(f"Result : {result}")