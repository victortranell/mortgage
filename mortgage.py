## Class for coloring output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## Tweakable parameters
intrest_reduction = 0.3 ## Ränteavdrag
yearly_income = """INSERT NUMBER HERE""" * 12
expected_salary_increase = 0.10

loan_amount = """INSERT NUMBER HERE"""
interest_rate = """INSERT NUMBER HERE"""
apartment_price = """INSERT NUMBER HERE"""
rent = """INSERT NUMBER HERE"""

inflation = 0.0 ## WIP: Will show how the loan is "eaten" by the inflation

## Initialize
amortization = 0 
cost = 0
year = 0

## Calculate and print monthly cost for the next 50 years
while year < 50:
    year += 1
    
    ## What if the ränteavdrag is decommissioned?
    # if year > 3:
    #     intrest_reduction = 0.2
    # if year > 4:
    #     intrest_reduction = 0.1
    # if year > 5:
    #     intrest_reduction = 0.0

    for month in range(1,12):
        percentage_of_property = loan_amount/apartment_price

        ## Ammorteringskrav
        if percentage_of_property > 0.7:
            print(bcolors.OKBLUE, end="")
            amortization = 0.02
        elif percentage_of_property < 0.7:
            print(bcolors.OKGREEN, end="")
            amortization = 0.01
        elif percentage_of_property < 0.5:
            print(bcolors.WARNING, end="")
            amortization = 0.0

        if loan_amount > yearly_income * 4.5:
            print(bcolors.FAIL, end="")
            amortization += 0.01

        monthly_intrest = loan_amount * interest_rate * (1 - intrest_reduction) / 12
        monthly_amortization = loan_amount * amortization / 12
        monthly_cost = monthly_intrest + monthly_amortization
        loan_amount -= monthly_amortization

        print(f'{year} {month} {monthly_cost + rent:.0f} {percentage_of_property*100:.1f}%')
        cost += monthly_cost
        
    loan_amount *= (1-inflation)
    apartment_price *= (1-inflation)

    ## What if your salary increases?
    yearly_income *= (1 + expected_salary_increase)

print(bcolors.ENDC)
