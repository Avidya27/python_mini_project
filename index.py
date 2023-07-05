#INCOME DETAILS
#using functions and loops
def income_details_function():
    c = int( input("Enter the number of income sourse(s):\t") )
    print("\n")
    total = 0

    for i in range(1,c+1):    
        x = int( input("Enter the income from source " + str(i) + ": " ) )
        total += x

    return (total)

#EXPENSES
#using function
def expenses_function():
    print("YOUR EXPENSES")
    common_string = "Enter the amount you spend on "

    print("---MONTHLY EXPENSES---\n")
    total_sum_1 = 0
    x1 = int( input(common_string + "Rent: ") )
    total_sum_1 += x1
    
    x2 = int( input(common_string + "Personal Expenses: ") )
    if x2 > 2000:
        print("SUGGESTION: Excessive expenditure on groceries")
    total_sum_1 += x2
    
    
    x4 = int( input(common_string + "Investments: ") )
    total_sum_1 += x4
    
    x5 = int( input(common_string + "Miscellaneous: ") )
    if x5 > 3500:
        print("SUGGESTION: Excessive expenditure on miscellaneous, try reducing it")
    total_sum_1 += x5
    
    print("\n\n===============================================================================\n")
    total_sum_2 = 0
    print("Major Yearly Expenses : ")
    x3 = int( input(common_string + "Student Loan: ") )
    total_sum_2 += x3
    
    x4 = int(input(common_string + "Taxes: "))
    total_sum_2 += x4
    
    total_expenses = total_sum_1 + (total_sum_2 / 12)
    return total_expenses


print("Ambatipudi Vidya")


#NOTIFICATIONS:
# Decision making and branching
while(True) :
    
    answer_1 = input("Would you like us to send you notifications?: ")    
    if answer_1 == "YES":
        print("Notifications are turned on.")
        break
        
    elif answer_1 == "NO":
        print("We wouldn't be able to update you.")
        break
        
    else:
        print("Please enter YES or NO.")
                 
print(type(answer_1))
print("\n========================================================================================")

#PERSONIAL DETAILS
print("----PERSONAL DETAILS----")

b1 = str( input("Enter your name: ") )
b3 = str( input("Enter your D.O.B: ") )

# Lamba functions
concat = lambda p, q : p + q

# String checking and loops
while(True) :
    b2 = str( input("Enter your password: ") )
    if b2 != concat(b1, b3) :
        print("Wrong password, try again")
        print("Password is concatenation of Name and DOB")
    else :
        break


print("\n----------------------------------------------------------------")

#using strings
print("personal_details_string_1: ", b1)
print("personal_details_string_2: ", b2)
print("personal_details_string_3: ", b3)
print("\npersonal_details_string_3[-1]: ", b3[-1])
print("personal_details_string_2[0:2]: ", b2[0:2])
print("\n----------------------------------------------------------------")


#using tuples
personal_details_tuple = (b1, b2, b3)
print("\npersonal_details_tuple: ", personal_details_tuple)
print("\npersonal_details_tuple[-1]: ", personal_details_tuple[-1])
print("personal_details_tuple[0:2]: ", personal_details_tuple[0:2])
print("\n----------------------------------------------------------------")
#using lists
personal_details_list = list(personal_details_tuple)
print("\npersonal_details_list: ", personal_details_list)
print("\npersonal_details_list[-1]: ", personal_details_list[-1])
print("personal_details_list[0:2]: ", personal_details_list[0:2])
print("\n=========================================================================")
total_income = income_details_function()
print("total income: ", total_income)
print("\n\n================================================================================")
