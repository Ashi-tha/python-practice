name = input("enter your full name ")

print(len(name))  #length of string

print(name.find(" "))  #to find the index of a character

print(name.rfind(" "))  #reverse index

print(name.capitalize()) #capitalize only the first letter

print(name.lower()) #change the entire string to lower case

print(name.upper()) #change the entire string string to upper case

print(name.isdigit()) #returns a boolean value ,to check whether the string  only contains digits

print(name.isalpha()) #returns a boolean value true , when the string only contains the alphabetical values

print(name.count()) # counts the appearence of the characters

print(help(str)) # provides a help manual , of different string methods

