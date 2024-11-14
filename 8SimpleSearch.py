#Below are the list of specific names that are valid to be entered
list_name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_n = input("Input name to search: ")

#To verify that the entered name is valid/in the list above
if search_n in list_name:
    print(f"Success! User {search_n} part of the list")
else:
    print(f"Access Denied! User {search_n} is not part of the list. Please input another user to try again")
