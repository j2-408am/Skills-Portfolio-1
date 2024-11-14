print("I am now counting from 0 to 50: ")
for i in range(51): #The range(51) actually goes from 0 to 50
    print(i, end=" ")
print() #Next sequence below

print("I am now counting down from 50 to 0: ")
for i in range(50, -1, -1): #Since it's counting down, this will start at 50 and will go to 0
    print(i, end=" ")
print()

print("I am now counting from 30 to 50: ")
for i in range(30, 51): #This will start at 30 until it reaches 50
    print(i, end=" ")
print()

print("I am now counting from from 50 to 10 by 2: ")
for i in range(50, 9, -2): #From 50, the starting point, it will eventually go to 9, then to the last number
    print(i, end=" ")
print()

print("I am now counting from 100 to 200 by 5: ")
for i in range(100, 201, 5): #This will start at 100, then to 201, then finally to 5
    print(i, end=" ")