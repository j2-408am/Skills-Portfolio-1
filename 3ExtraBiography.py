#This is where the user will be the one to input their own information
user = {}
user ['user_name'] = input("Please enter your name: ") #Will get the user's name
user ['user_home'] = input("Please enter your hometown: ") #Will get the user's hometown

while True:
    try: #Only used for testing code execution
        user_age = input("Please enter your age: ") #If the user where to input a string value for age, the program will let it slide and accept it.
        user ['user_age'] = int(user_age)
        break
    except ValueError: #For handling any errors in the program
        print("Only numerical value is accepted.")
        print("Please try again")

#The final step where all information will be printed according to the information entered.
print("Your information")
print("Your name is:" + user['user_name'])
print("Your hometown is:" + user['user_home'])
print("Your current age is:" + str(user['user_age']))