#necessary imports
import matplotlib.pyplot as plt
from math import pow

#declaring the class morgage
class morgage:
    def __init__(self, loan, years, interest, r_frequency):
        #instance variables
        self.loan = loan
        self.years = years
        self.interest = interest /100
        self.r_frequency = r_frequency
        self.p0 = self.repayments()
    
    #repayments method
    def repayments(self):
        #didiving the repayment method to parts inorder to reduce complexity
        equation_1 = self.loan * (pow(1+(self.interest/365), 365 * self.years))
        equation_2 = pow(1+(self.interest/365), self.r_frequency) - 1
        equation_3 = pow(1+(self.interest/365), 365 * self.years) - 1
        p0 = equation_1 * (equation_2/equation_3)
        return p0 # the return value for self.repayments

    #balance sheet method
    def balance_after(self, n):
        equation_4 = self.loan * pow(1+ (self.interest/365), 365*n)
        equation_5 = pow(1+ (self.interest/365), 365*n) - 1
        equation_6 = pow(1+ (self.interest/365), self.r_frequency) -1
        bn = equation_4 - self.p0 * (equation_5/equation_6)
        return bn


    #str method 
    def __str__(self):
        return (f' Loan Amount: {self.loan} AUD \n Loan Term (Years): {self.years} \n Interest: {self.interest * 100} % \n Repayment Amount: {round(self.p0, 2)} for every {self.r_frequency} days')
    
    #drawing line graph
    def draw_balance_graph(self):
        years_array = []
        #getting the years array
        for i in range(0, self.years+1):
            years_array.append(i)
        balance_array = []
        #calcuating the balance after every year
        for j in years_array[:]:
            balance = self.balance_after(j)
            balance_array.append(balance)
            
        plt.plot(years_array, balance_array, marker='o', linestyle='-')
        plt.xlabel("Years") #xlabel
        plt.ylabel("Balance") #ylabel
        plt.title("Morgage Balance by Years") #titlename
        plt.grid(True)  # Add grid lines
        plt.gca().set_facecolor('lightgray')  # Add a light gray background
        plt.gca().spines['top'].set_color('black')  # Add a border
        plt.gca().spines['bottom'].set_color('black')
        plt.gca().spines['left'].set_color('black')
        plt.gca().spines['right'].set_color('black')

        plt.show()

