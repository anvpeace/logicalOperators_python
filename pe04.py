""" 
4.  
Implement the following to simulate how websites ensure that everyone has a unique username.  
a) Make a list of five or more usernames called current_users.  
b) Request an input of username.  
c) Print a message, Sorry XXX, that name is taken and also display the current user list if the input username has already been used.  XXX is the input user name.  
d) Print a message, Great, XXX is still available and also display the updated user list if the username has        not been used.  
e) Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' or ‘john’ should not be accepted. 
"""

current_users = ["gamergames0070", "jappleceed123", "pacman222", "mario64", "luigi19", "john"]

username = input("Enter a username: ")

if username:
    print(f'Sorry {username}, that name is taken.\n')
    print("\nThese are the taken usernames")
    for user in current_users:
        print(user)
username = ""
# for user in current_users:

#     username == user.title() and username == user.upper() and username == user.lower()

username = input("Enter a username: ")

if username != current_users:
    
    current_users.append(username)
    print(f'Great, {username} is still available \n', current_users)

# elif username == user.title() and username == user.upper and username == user.lower:
#     print(f'Sorry {username}, that name is taken.\n')
