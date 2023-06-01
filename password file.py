
#Maxine Silverman 
#Rock Paper Scissor
#password keeper : this code will keep track of usernames and passwords for different websites 
#challenges : Allow the user to access either website’s, usernames or password
import sys
websites = []
usernames = []
passwords = []
entries = 0

while True:
    entry = input("New entry? yes/no: ")

    if entry == "no":
        if entries == 0:
            print("No entries, program ended")
            sys.exit()
        break
    elif entry == "yes":
        entries += 1
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        websites.append(website)
        usernames.append(username)
        passwords.append(password)
    else:
        print("Invalid")

while True:
    mode = input("What would you like to see ? Pick a number :  1. See everything  2. See all passwords 3. See all usernames  5. Exit")
    

    if mode == "1":
        for index in range(len(websites)): 
            print(websites[index])
            print(usernames[index])
            print(passwords[index])
            print()
    elif mode == "2":
        for index in range(len(websites)):
         print(passwords[index])
    elif mode == "3":
        for index in range(len(websites)):
         print(usernames[index])

    elif mode == "4":
        break

    else:
        print("Invalid")