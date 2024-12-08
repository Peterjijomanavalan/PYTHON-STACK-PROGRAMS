def power(base, exponent):
    return base ** exponent  # Using the power operator ** to calculate base^exponent
ch = 'y'
while ch.lower() == 'y':
    base = float(input("\nEnter the base: "))
    exponent = int(input("Enter the exponent: "))
    result = power(base, exponent)# Calculate the result
    print(f"{base} raised to the power of {exponent} is {result}")
    ch = input('PRESS [Y|N] TO CONTINUE: ') # Ask if the user wants to continue
    if ch.lower() not in ['y', 'n']:
        print("Invalid input. Please enter 'Y' or 'N'.")
        ch = 'y'  
