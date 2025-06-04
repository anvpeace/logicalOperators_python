""""
A 

print(a ** b == b ** a) 

B 

print(a < b or b < a) 

Output  Output  

C 

print('dog' > 'cat' + 'mouse') 

D 

print('Car' < 'Train') 

Output  Output  

E 

print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b))) Output  

F 

print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b))) Output  
G 

print(not ((a < b) and (a < (b + a)))) Output  
H 

print("small" > "large" and (not c )) Output  
I 

print(isinstance(c, int)) J print(isinstance(3.14, float)) Output  Output  
K 

if (a < b < c):     
    
    b = c + a 
    
    else: b = c * a 
    
print(b) 

L 

if ('A' in 'apple'):     
    
    print("A as apple." ) 
    
else:     
    
    print('Oops, not there.') 
    
    Output  Output 
    
M 

x = 6 if (x < 0):     

print('negative') 

else:     
    
    if (x == 0):         
        
        print('zero')     
        
        else:    
            
            print('positive')
            
N 

n = 1 

if n <= 9:     

print ("Less than ten.") 

elif n == 1:     
    
    print("Equal to one.") 
    
    Output  Output 
    
O 

let = input("Enter A, B or C: \n") 

let = let.upper()  

if (let == 'A'):     
    
    print('\nA, my name is Alice.') 
    
    elif (let == 'B'):    
        
        print('\nTo be, or not to be.')
        
        
elif (let == 'C'):    
    
    print('\nOh, say, can you see.') 
    
    
    else: print('\nInvalid letter.') 

"""
a = 2

b= 3

c = 0

# A 


print(a ** b == b ** a)

# Output 
# False




# B 

print(a < b or b < a) 

# Output  
# True

# C 

print('dog' > 'cat' + 'mouse') 
# Output 
# True

# D 

print('Car' < 'Train') 

# Output
# True

# E


print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b))) 

# Output
# False 

# F 

print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b))) 

# Output 
# True 

# G 

print(not ((a < b) and (a < (b + a)))) 

# Output 
# False 

# H 

print("small" > "large" and (not c )) 

# Output  
# True

# I 

print(isinstance(c, int)) 
# Output
# True


# J 
print(isinstance(3.14, float)) 

# Output
# True


# K 

if (a < b < c):     
    
    b = c + a 
    
else: b = c * a 
    
print(b) 

# Output
# 0


# L 

if ('A' in 'apple'):     
    
    print("A as apple." ) 
    
else:     
    
    print('Oops, not there.') 
    
# Output 
# "Oops, not there"
    
# M 

x = 6 

if (x < 0):     

    print('negative') 

else:     
    
    if (x == 0):         
        
        print('zero')     
        
    else:    
            
        print('positive')

# Output
# positive
            
# N 

n = 1 

if n <= 9:     

    print ("Less than ten.") 


elif n == 1:     
    
    print("Equal to one.") 
    

# Output 
# "Less than ten."
    
# O 

let = input("Enter A, B or C: \n") 

let = let.upper()  

if (let == 'A'):     
    
    print('\nA, my name is Alice.') 
    
elif (let == 'B'):    
        
        print('\nTo be, or not to be.')
        
        
elif (let == 'C'):    
    
    print('\nOh, say, can you see.') 
    
    
else: print('\nInvalid letter.') 


# output
# Enter A, B or C: