""" 5.  Implement the following to search a letter in a list.   
a) Create a list named vehicles: car, Truck, boat, PLANE.   
b) Request a user input for a search letter.  
c) Use the decision structure in a for loop to search all the items which contains the input letter (ignoring case) in the list.  

d) Print the item and its position in vehicles if it exists.  Otherwise, print the statement indicating it does not      contain the letter to search.  
e) Print the error message if more than one letter is entered. """

# a) Create a list named vehicles: car, Truck, boat, PLANE.   
vehicles = ["car", "truck", "boat", "PLANE"]

# b) Request a user input for a search letter.  
search = input("Eneter a letter to search: ").split(" ")

# searchList = list(search)
# print(searchList)

# c) Use the decision structure in a for loop to search all the items which contains the input letter (ignoring case) in the list.  

for car in vehicles:

    if search == car:
        print(car)
print()



# d) Print the item and its position in vehicles if it exists.  Otherwise, print the statement indicating it does not      contain the letter to search.  

