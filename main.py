#importing morgage class from morgage.py
from morgage import morgage

#functions for error handling when taking inputs from the user
def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Invalid input. Please enter a positive number. Try again...")
        except ValueError:
            print("Invalid input. Please enter a valid number. Try again...")

def get_positive_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Invalid input. Please enter a positive integer. Try again...")
        except ValueError:
            print("Invalid input. Please enter a valid integer. Try again...")

def get_interest(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 30:
                return value
            else:
                print("Inerest rate is greater than 30. Try again...")
        except ValueError:
            print("Invalid input. Please enter a valid input. Try again...")
def get_r_frequency(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value == 7 or value == 14 or value == 30:
                return value
            else:
                print("Invalid input. Value must be 7, 14, or 30. Try again...")
        except ValueError:
            print("Invalid input. Please enter a valid input. Try again...")

#taking input for the different class attributes
loan = get_positive_float_input("Enter the loan Amount in AUD: ")
years = get_positive_int_input("Enter a loan term in years: ")
interest = get_interest("Enter the bank's interest rate in %: ")
r_frequency = get_r_frequency("Enter the repayment frequency in days (7, 14 or 30): ")

#declaring and initializing a class using the attributes obtained above
person_1 = morgage(loan, years, interest, r_frequency)
print(person_1)

# funtion for determining whether to display the line graph or not
def show_graph():
    while True:
        try:
            graph_prompt = input('Would you like to plot the "Balance by Years" graph? (y, n): ')
            if graph_prompt.lower().startswith('y'):
                person_1.draw_balance_graph()
                break  
            elif graph_prompt.lower().startswith('n'):
                print('Thamk you for your time')
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        except Exception as e:
            print("An error occurred:", e)

#calling the function above
show_graph()