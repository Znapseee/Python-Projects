# PART 1: Create a function that is based on four mathematical operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# PART 2: Create a dictionary of operations
math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# PART 3: Create a loop that will keep the keep the calculator operating
print("""
_________     _____  .____   _________  ____ ___.____       ________________________ __________ 
\_   ___ \   /  _  \ |    |  \_   ___ \|    |   \    |     /  _  \__    ___/\_____  \\______   \
/    \  \/  /  /_\  \|    |  /    \  \/|    |   /    |    /  /_\  \|    |    /   |   \|       _/
\     \____/    |    \    |__\     \___|    |  /|    |___/    |    \    |   /    |    \    |   \
 \______  /\____|__  /_______ \______  /______/ |_______ \____|__  /____|   \_______  /____|_  /
        \/         \/        \/      \/                 \/       \/                 \/       \/ 

""")

is_continue = True

try:
    while is_continue:
        to_operate = str(input("Enter YES to continue and NO if not: ")).lower()

        if to_operate == 'no':
            is_continue = False 
            print("Thank you for using the simple calculator")
    
        elif to_operate == 'yes':
            n1 = float(input("Enter the first value: "))
            n2 = float(input("Enter the second value: "))
            operations = input("Enter the desired operation (add/subtract/multiply/divide): ").lower()
        
            if operations == "add":
                sum_result = math_operations["+"](n1, n2)
                print(f"The value of {n1} + {n2} is {sum_result}")

            elif operations == "subtract":
                difference_result = math_operations["-"](n1, n2)
                print(f"The value of {n1} - {n2} is {difference_result}")

            elif operations == "multiply":
                product_result = math_operations["*"](n1, n2)
                print(f"The value of {n1} x {n2} is {product_result}")

            elif operations == "divide":
                quotient_result = math_operations["/"](n1, n2)
                print(f"The value of {n1} / {n2} is {quotient_result}")
                
            else:
                print("Enter a valid operation.")
    
except:
    print("An error occurred. Please enter a valid operation. ")

