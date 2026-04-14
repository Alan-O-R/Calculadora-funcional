import math

def sqrt():
    operation== "sqrt" == "s"
print("""
      
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▄▀█ █░░ ▄▀█ █▄░█ ▀ █▀   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▀█ █▄▄ █▀█ █░▀█   ▄█   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄

""")
print("please chose the operation")
operation = input("+, -, *, /, s , **: ")   
first_number = input("\nfirst number:")
if operation != "s":
    sqrt()
    second_number= input("second number:")
try:
    if operation == "+":
        print("\nThe result is:", round(float(first_number) + float(second_number)))
    elif operation == "-":
        print("\nThe result is:", round(float(first_number) - float(second_number)))
    elif operation == "*":
        print("\nThe result is:", round(float(first_number) * float(second_number)))
    elif operation == "/":
        print("\nThe result is:", round(float(first_number) / float(second_number)))
    elif operation == "s":
        resultado = math.sqrt(float(first_number))
        if resultado != int(resultado):
            print("\nThe result is:", f"{resultado:.2f}")
        else:
            print("\nThe result is:", int(resultado))
    elif operation == "**":
        print("\nThe result is:", round(float(first_number) ** float(second_number)))
    else:
        print("\nInvalid operation")
except ValueError:
    print("\nInvalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("\nError: Division by zero is not allowed.")

    
print("\nThanks for using Alan's Calculator!")






                            