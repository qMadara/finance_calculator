# Name: Mmedara Udongwo
# Student ID: 2334019
# Date: 06/11/2024
''' This is a simple Personal Finance Calculator that allows the user input thier monthly
track expenses and provide basic analysis'''

print("Welcome to Personal Finance Calculator")
print("")

# Initialize variables as 0
inc = 0
exp = 0
essential = 0
non_essential = 0
Total_expense = 0 
Total_income = 0

# This function is used to get the user input thier income
def income():
    global inc 
    global Total_income
    inc = float(input("Enter your monthly income: "))
    
    # Used to print an error message if the income entered is less than or equal to 0
    if inc <= 0:
        print("Error: Your income input is invalid. Try again")
        inc = float(input("Enter your monthly income: "))
    print("Income recorded successfully")    
    # add user inputted income to total income   
    Total_income += inc
    print("")
    
# This function is used to get the user input thier expenses and expense category
def expense():
    global exp
    global essential
    global non_essential
    global Total_expense
    exp = float(input("Enter expense amount: "))
    Total_expense += exp
    
    # Get user to input if expense is essential/non-essential
    essential_exp =  input("Enter expense category (essential/non-essential):")
    
    # print an error message if entered input is neither essential nor non-essential
    if essential_exp != "essential" and essential_exp != "non-essential" :
        print("Error: Your input is invalid. Try again")
        essential_exp =  input("Enter expense category (essential/non-essential):")
    print(f"Expense added, categorized as {essential_exp}")    
    # if user input is essential add user expense to essential    
    if essential_exp == "essential":
        essential += exp
        
    # if user input is non-essential add user expense to non essential     
    elif essential_exp == "non-essential":
        non_essential += exp
        
    # if conditions are not met continue with the program    
    else :
        expense()
    print("") 
      
# This function is used to calculate the budget breakdown     
def summary():
    
    # the variable is used to get the remaining budget
    remaining_budget = Total_income-Total_expense
    
    # this command is used to print the outputs
    print(f"Income: £{Total_income}")
    print(f"Total Expenses: £{Total_expense}")
    print(f"Remaining Budget: £{remaining_budget} ")
    
    # the variable is used to calculate amount the user is expected to save
    savings = remaining_budget/2
    
    # if user remaining budget is less than 0, print a message(Over budget)
    if remaining_budget < 0:
        print("You're over budget.")
        
    # if user remaining budget is greater than 0, prompt user to save 50% of remaining budget    
    else:
        print(f"You're under budget. Consider saving £{savings} (50% of remaining budget)")
        print("")
        print("Expense Breakdown:")
        print(f"Essential: £{essential}")
        print(f"Non-essential: £{non_essential}")

    
# This function is used for the selection    
def option():
    while True:
        print("1. Enter income\n" 
              "2. Add Expense\n"
              "3. View Budget Summary\n"
              "4. Exit \n")
        user_choice = input("Enter your choice: ")
         
        if user_choice == "1":
           income()
        elif user_choice == "2":
            expense()
        elif user_choice == "3":  
            summary()  
        elif user_choice == "4":
            print("Thank you for using Personal Finance Calculator!")
            break
        else:
            print("Option selected is invalid") 
option()            
              

    

