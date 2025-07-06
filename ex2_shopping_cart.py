#ex 2 shopping cart program
item = input("what item do you like to buy?:")
price= float(input("what is the price?"))
quantity=int(input("how many would you like?"))
total= quantity*price
print(f"you have bought{quantity} x {item}/s")
print(f"your total is {total}")