"""
2.  Write an if-elif-else chain that determines a person’s stage of life.   

a) Set your age for the variable age.  

b) If the age is less than 0, print an error message, invalid age.  

c) If the age is less than 2 years old, print a message, you’re a baby.  d) If the age is at least 2 years old but less than 4, print a message, you’re a toddler.  
e) If the age is at least 4 years old but less than 13, print a message, you’re a kid.  
f) If the age is at least 13 years old but less than 20, print a message, you’re a teenager.  
g) If the age is at least 20 years old but less than 65, print a message, you’re an adult.  
h) If the age is 65 or older, print a message, you’re an elder.   

Example Output  Age = 20  You’re an adult. 

"""

age = int(input("Enter your age: "))

if age <= 0:
    print("invalid age")
    
elif age <= 2:
    print(f'Age: {age}' + "you're a baby.")

elif age >= 13 and age <= 20:
    print(f'Age: {age}' + "you're a teenager.")
    
elif age >= 20 and age <= 65:
    print(f'Age: {age}' + "you're an adult.")
else:
    if age > 65:
        print(f'Age: {age}' + "you're an elder.")
