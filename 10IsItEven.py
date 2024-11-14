def checkno_odd_even(num_user):
    #For checking if the number is odd or even
    if num_user % 2 == 0:
        return f"Even-Steven!It is confirmed that {num_user} is even!"
    else:
        return f"Bob-the-Odd! It is confirmed that {num_user} is odd!"

def main():
    try:
        #The user will now input the number they want to enter
        num_user = int(input("Please enter your chosen number: "))
        #Result will then follow after inputting the number through the first function checkno_odd_even(num_user)
        result = checkno_odd_even(num_user)
        print(result)
    except ValueError:
        print("Error! Only valid number is allowed in this program.")
        
if __name__ == "__main__":
    main()