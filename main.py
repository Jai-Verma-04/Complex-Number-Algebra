from time import sleep

def add_complex(first, second):
    ans = first + second
    return ans

def subtract_complex(first, second):
    ans = first + second
    return ans

def divide_complex(first, second):
    ans = first + second
    return ans

def multiply_complex(first, second):
    ans = first + second
    return ans

def ask_first_num():
    print("Enter the parts of first complex number below: ")
    first_real = int(input("Enter the real part of the first number: "))
    first_complex = int(input("Enter imaginary part[without i]"))
    first_num = complex(first_real, first_complex)
    return first_num

def ask_second_num():
    print("Enter the parts of second complex number below: ")
    second_real = int(input("Enter the real part of the second number: "))
    second_complex = int(input("Enter imaginary part[without i]"))
    second_num = complex(second_real, second_complex)
    return second_num

running = True
while running:
    print("\nWelcome to complex number calculator.")
    print("Please select an option from below")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Which operation do you want to perform? "))

    if choice>4 or choice<1:
        print("Please select correct option.")
        sleep(1)
        continue
    else:
        if choice == 1:
            first_num = ask_first_num()
            second_num = ask_second_num()
            ans = add_complex(first_num, second_num)
            print("Result: ",ans)
            

        elif choice ==2:
            first_num = ask_first_num()
            second_num = ask_second_num()
            ans = subtract_complex(first_num, second_num)
            print("Result: ",ans)
            

        elif choice == 3:
            first_num = ask_first_num()
            second_num = ask_second_num()
            ans = multiply_complex(first_num, second_num)
            print("Result: ",ans)
            

        elif choice == 4:
            first_num = ask_first_num()
            second_num = ask_second_num()
            ans = divide_complex(first_num, second_num)
            print("Result: ",ans)
            
    ask = input("press q to quit or any other key to continue").lower()
    
    if ask == 'q':
        quit()
    else:
        continue