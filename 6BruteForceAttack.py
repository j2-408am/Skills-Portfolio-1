my_pass = "12345"
attempts = 5
    
#Variables
trial = 0
log_accept = False
    
print("Welcome, dear user")
print("Please input password to proceed")
    
#For when login is being attempted
while trial < attempts and not log_accept:
    #To be specific, this code will calculate the remaining attempts left
    remaining_trial = attempts - trial 
    print(f"\nAttempts Remaining: {remaining_trial}")
        
    #Where user will input the password
    pass_trial = input("Please input your valid password: ")

    #Password checker
    if pass_trial == my_pass:
        log_accept = True
        print("\nAccess granted. Welcome back, dear user!")
    else:
        trial += 1
        if trial < attempts:
            print("Access Denied!! Please enter your correct password.")
        else:
            print("Warning: Security has been alerted. Authorized people have been notified")