# Simple Multitool Calculator program by @berhocode
# Multicalc program

                    # --- basic calculator functions ---

def calculator():
    def addition():
        print("Result: ", float(x) + float(y))

    def subtraction():
        print("Result: ", float(x) - float(y))

    def multiplication():
        print("Result: ", float(x) * float(y))

    def division():
        if float(y) == 0 or float(x) == 0:
            print("Error: Division by zero")
        else:
            print("Result: ", float(x) / float(y))
            
    # new functions added:

    def modulus():
        print("Result: ", float(x) % float(y))

    def power():
        print("Result: ", float(x) ** float(y))

    # --- calculator ---

    while True:
        print("Enter the first number ~ (Q)uit:")
        x = input("> ")
        if x.upper() == "Q":
            program_name = "calculator"
            print(f"Exit {program_name} program...")
            break
        print("Enter the operator (+,-,*,/,%,**)")
        opr = input("> ")
        print("Enter the second number:")
        y = input("> ")
        if opr == "+":
            addition()
        elif opr == "-":
            subtraction()
        elif opr == "*":
            multiplication()
        elif opr == "/":
            division()
        elif opr == "%":
            modulus()
        elif opr == "**":
            power()
        else:
            print("Invalid input, please try again or type 'Q' to exit!")
        
# kg to Lbs

def kg_to_Lbs():
     while True:
        Weight = input("Weight ~ (Q)uit: ")
        if Weight.upper() == "Q":
            program_name = "Kg to Lbs"
            print(f"exit {program_name} program...")
            break
        Choose_K_or_L = input("(K)g or (L)bs: ")

        if Choose_K_or_L.upper() == "K":
            print("Weight in lbs", float(Weight) / 0.45 )
        elif Choose_K_or_L.upper() == "L":
            print("Weight in Kg",float(Weight) * 0.45)
        else:
            print("Invalid inputs, Pls try again!")
        

# Check the number if it's ODD or EVEN

def odd_or_even():
     while True:
        number = input("Enter a number to define if it's ODD or EVEN -(Q)uit-: ")
        if number.upper() == "Q":
            program_name = "ODD or EVEN"
            print(f"exit {program_name} program...")
            break
        print("EVEN" if float(number) %2 == 0 else "ODD")

        # ODD: x % 2 = 0
        # EVEN: x % 2 = *0

#-----------------------------------------------------------------------------------

# calculate the number of digits in a number


def num_digits():
     while True:
        number = input("Number ~ (Q)uit: ")
        if number.upper() == "Q":
            program_name = "number digits"
            print(f"exit {program_name} program...")
            break
        num_d = len(number)
        if (number).isdigit() == True:
            print("Number digits equal to ",num_d)
        else:
            print("pls enter a number!")

        


# Celcius to Fahrenheit

def C_to_F():
    while True:
        temp = input("Enter the temperatur ~ (Q)uit: ")
        if temp.upper() == "Q":
            program_name = "Celcius to Fahrenheit"
            print(f"exit {program_name} program...")
            break
        temp_unit = input("(C)elcius or (F)ahrenheit: ")

        if temp_unit.upper() == "C":
            temp = round((float(temp) * 9 / 5) + 32, 2)
            print(f"Temperature in Fahrenheit: {temp}°F")

        elif temp_unit.upper() == "F":
            temp = round((float(temp) - 32) * 5 / 9, 2)
            print(f"Temperature in Celcius: {temp}°C")

        else:
            print(f"{temp_unit} or {temp} are invalids, Pls try again!")


# Deg to rad
def deg_to_rad():
    pi = 3.141592653589793
    while True:
        degrees = input("Enter angle in degrees ~ (Q)uit: ")
        if degrees.upper() == "Q":
            program_name = "Deg to Rad"
            print(f"Exit {program_name} program...")
            break
        if degrees.isdigit():  # Check if the input is numeric
            radians = float(degrees) * (pi / 180)
            print(f"{degrees} degrees is equal to {radians} radians.")
        else:
            print("Invalid input, please enter a numeric value or 'Q' to quit.")


# --- Full program ---


while True:
    print("""---------
*Choose* ~ *(Q)uit* :
~ (C)alculator 
~ Kg to Lbs (KB) 
~ Celcius to Fahrenheit (CF)
~ Odd or even (OE) 
~ nbr digits (ND)
~ Deg to Rad (DR):
---------""")
    User_Choose = input("> ").upper()
    if User_Choose == "C":
        calculator()
    elif User_Choose == "KB":
        kg_to_Lbs()
    elif User_Choose == "CF":
        C_to_F()
    elif User_Choose == "OE":
        odd_or_even()
    elif User_Choose == "ND":
        num_digits()
    elif User_Choose == "DR":
        deg_to_rad()
    elif User_Choose == "Q":
        break
    else:
        print(f"{User_Choose} is not available, Pls try again...")
