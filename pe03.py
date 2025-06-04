""" 
3.  Implement the following to print a greeting to each user after they log in to a website.   
a) Make a list of five usernnames, including the name “admin”.  
b) Loop through the list and print a greeting to each user.  
c) If the username is “admin”, print a special greeting, such as       Hello Admin, would you like to see a status report?  
d) Otherwise, print a generic greeting, such as       Hello Eric, thank you for logging in again!  
*e) Implement if the list is empty by printing the message, We need to find some users.  
 Example Output 1:  
 Hello Tom, thank you for logging in again!  
 Hello Jerry, thank you for logging in again!  
 Hello Bob, thank you for logging in again!  
 Hello Dora, thank you for logging in again!  
 Hello ADMIN, would you like to see a status report?     
 
 Example Output 2 (if the list is empty)  We need to find some users. """

userNames = ["Jerry", "Kennedy", "Will", "Mary", "admin"]

login = input("Enter your user name: ")

for user in userNames:

    if login == user in userNames:
        print(f'Hello {user}, thank you for logging in again!')

    if login in user == "admin":
        print(f'Hello {user}, would you like to see status report?')
else:
        if userNames == [] or login != user:
            print("We need to find some users.")

