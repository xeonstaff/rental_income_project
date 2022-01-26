"""
1. I decided against the 'input' function because it just seems silly if these
programs aren't going to be used front-end. Maybe there's somtehing I don't understand but.
I guess a nice GUI would be the best option, but I wouldn't know where to start.

2. A test instance is written below so you can just run this bish as an example.

"""

class RentalProp:
    #class variables generated from methods
    income = 0 
    expenses = 0
    cashflow = 0
    investment = 0
    roi=0

    def __init__(self, address, city):
        self.address = address
        self.city = city  

    def income_calc(self, rental_income,other_income):
        self.income = rental_income + other_income
        return(f"This property should make ${self.income} per month.")

    def expenses_calc(self, tax, insurance, utilities, prop_management, vacancy, other):
        self.expenses = tax + insurance + utilities + prop_management + vacancy + other
        return(f"This property should cost ${self.expenses} per month.")

    def investment_calc(self, down_payment, closing_costs, rehab_budget):
        self.investment = down_payment + closing_costs + rehab_budget
        return(f"Your total property investment is ${self.investment} per month.")

    def roi_calc(self):
        self.cashflow = self.income - self.expenses
        self.roi = round((self.cashflow/self.investment * 100),2)
        roi_adj = ""
        if self.roi < 1:
            roi_adj="horrible & atrocious"
        elif 1 <= self.roi < 3:
            roi_adj = "pretty bad"
        elif 3 <= self.roi < 5:
            roi_adj = "acceptable"
        elif 5 <= self.roi < 10:
            roi_adj = "reasonable"
        elif 10 <= self.roi:
            roi_adj = "pretty great"

        print(f"Your ROI is {self.roi}%. This return is {roi_adj}.")

#generating sample instance, testing attributes 
first_house = RentalProp("100 Birch Ln Ct Dr", "Odessa")
print(first_house.city)

#testing the income_calc method
print(first_house.income_calc(2000,1000))
print(first_house.income)

#testing the expenses_calc method
print(first_house.expenses_calc(200,300,200,200,100,200))
print(first_house.expenses)

#testing the investment_calc method
print(first_house.investment_calc(30000,4000,20000))
print(first_house.investment)

#testing the roi_calc method
first_house.roi_calc()



















