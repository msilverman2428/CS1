
#Maxine Silverman 
#Online Calculator - Ask user to pick 1-7 options for their online calculator 
#challenges: exponent function
# challenges : create the sumn function so the user can either put in an integer right away or stop right away 


def add(num_1, num_2) : # creates a function for addition
    print(num_1 + num_2) #when addition fucntion is called add two numbers 
def subtract(num_1, num_2): # create a subtratction function 
    return num_1 - num_2 # when subtraction function is called subtract the two numbers 
def check_int(): #checks to see if the two numbers are integers 
    while True: #creates loop 
        num = input("enter a value: ") # promps user to enter num 1
        try: # test the number out to see if its an integer
            return int(num) # if it is ask them to put in second number 
        except ValueError: # if not an integer, 
            print("Please enter an integer!") # tell user to put in int
def multiply(): # defining mulpitplcation as a function
    num_1 = check_int() #check if num 1 is an int
    num_2 = check_int() #check if num 2 is an int
    return num_1 * num_2 # print num1 times num2 if this funct is called 
def divide():  # create a function for division 
    num_1 = check_int() # check if num 1 is int
    num_2 = check_int() #check if num 2 is int 
    return num_1 / num_2 # print out num1 divided by num2
def exponent(): # create a function for exponents 
    num_1 = check_int() #check if num 1 is a int
    num_2 = check_int() #check if num 2 is int 
    return num_1 ** num_2 # print num 1 ^ of num 2

def sum(numbers): # create a function for sum that takes a list of int
    total = 0

    for number in numbers:
        total += number

    return total # returns the sum for all the int 

def main(): #gives user option for which function 
   while True: #loop 
       choice = input('''select operation  
     1. Add
     2. Subtract
     3. Multiply
     4. Divide
     5. Sum
     6. Exponent
     7. Quit''') # Asks user which operation they wna pick 

       if choice == "1": # if user puts 1 
           num_1 = check_int() #chgeck if its int 
           num_2 = check_int() #check if its int 
           add(num_1, num_2) # add two ints 

       elif choice == "2":  #if its choice 2 
           num_1 = check_int() #check if its int 
           num_2 = check_int() #check if its int 
           print(subtract(num_1, num_2)) #subtact two ints 

       elif choice == "3": # if its choice 3 
           print(multiply()) # multiply two ints 

       elif choice == "4": #if choice 4 is picked 
           print(divide())  #divide two ints 
       elif choice == "5": # if its choice 5 
           numbers = [] #prompt user to input a list of numbers 

           while True:
               num = input("Enter an integer or stop to get sum: ") # tell user if they wna stop putting ints input "stop" if not keep putting in integers             
               if num.lower() == "stop": # if user inputs "stop"
                   break #end this function 
               else: # if not stop 
                   try:
                       numbers.append(int(num)) # keep adding integers the user puts in 
                   except ValueError: # if the input isnt an int 
                       print("Please enter stop or a number!") # ask user to enter an integer 
           print(sum(numbers)) # return the sum of all the numbers 

       elif choice == "6": # if user picks 6 
           print(exponent()) # print exponent function 

       elif choice == "7": # if user picks 7 
           break # end code 
       else: # if all of those arent picked 
           print("Please enter a valid option")  # prompt user to pick a number 1-7

main() # run the main function 