def main():

            # using defination function

    def fahrenheit_to_celsius():
        F = int(input("Enter the temp. in fahrenheit: "))
        C = round((F - 32) * 5/9 , 2)
        print(f"The temp. in celsius is {C}")
        
    def celsius_to_fahrenheit():
        C = int(input("Enter the temp. in celsius: "))
        F = round((9/5 * C + 32) , 2)
        print(f"The temp. in fahrenheit is {F}")

    print("Welcome to Temperature Converter.")

    a = int(input('''
    What would you like to convert:
    1. Fahrenheit to Celsius
    2. Celsius to Fahrenheit
    '''))
            # using if statements
    if a == 1:
        fahrenheit_to_celsius()

    elif a == 2:
        celsius_to_fahrenheit()
    
    else:
        print("Invalid Input.")
    

while True:
    main()
    user_input = input('Do you want to run the program again? yes / no :').strip().lower()  
    if user_input not in ['yes' , 'y']:
        print('Exiting...')
        break