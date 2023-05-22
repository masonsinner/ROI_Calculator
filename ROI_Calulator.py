from time import sleep

class Calulator:

#SET UP STORAGE FOR VALUES
    def __init__(self):
        self.income_dict = {}
        self.expenses_dict = {}
        self.total_investment_dict = {}
        self.cash_roi_dict = {}

#GET MONTHLY INCOME
    def get_income(self):
        print('\nWelcome to Bigger Pockets!\nAre you ready to 10x your income!')
        sleep(3)
        print('\nFor the following questions will be for monthly income. \nPlease fill it out accordingly for the most accurate results.')
        sleep(3)
        
        while True:
            rent_income = input("\nWhat is your income from your property/properties: ")
            if rent_income.isnumeric():
                self.income_dict['rental'] = int(rent_income)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")

        while True:
            laundry_income = input('\nDo you have any income from laundry: ')
            if laundry_income.isnumeric():
                self.income_dict['laundry income'] = int(laundry_income)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")

        while True:
            storage_income = input('\nDo you have any income from storage: ')
            if storage_income.isnumeric():
                self.income_dict['storage income'] = int(storage_income)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")

        while True:
            misc_income = input('\nDo you have any other miscellaneous income: ')
            if misc_income.isnumeric():
                self.income_dict['miscellaneous income'] = int(misc_income)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")

        print(self.income_dict)

#GET MONTHLY EXPENSES
    def get_expenses(self):
        print("\nTerrific, let's move onto the expenses!")
        sleep(3)
        print("\nKeep in mind these are monthly expenses. \nProviding false information WILL affect the ROI")
        sleep(3)
    
        while True:
            tax_insurance = ['tax', 'insurance']
            for tax_insurance in tax_insurance:
                while True:
                    tax_insurance_amount = input(f"How much do you spend on {tax_insurance}: ")
                    if tax_insurance_amount.isnumeric():
                        self.expenses_dict[tax_insurance] = int(tax_insurance_amount)
                        break
                    else:
                        print("I'm sorry, but this should be a number. \nPlease try again.")
            break

        
        while True:
            utilities = input("Do you pay for utilities? (yes/no): ")
            sleep(3)
            if utilities.lower() == 'yes' or utilities.lower() == 'y':
                expenses_list = ['electric', 'water', 'sewer', 'garbage', 'gas']
                for expense in expenses_list:
                    while True:
                        expense_amount = input(f"How much do you spend on {expense}: ")
                        if expense_amount.isnumeric():
                            self.expenses_dict[expense] = int(expense_amount)
                            break
                        else:
                            print("I'm sorry, but this should be a number. \nPlease try again.")
                    expenses_entered = True
                if expenses_entered:
                    print(f"Here are your expenses: {self.expenses_dict}")
                    break
            elif utilities.lower() == "no" or utilities.lower() == 'n':
                print("Way to save some on expenses!")
                print(f"Here are your expenses with utilities: {self.expenses_dict}")
                break
            else:
                print("I'm sorry that is not one of the options")

            sleep(3)

            print(f"Here are your expenses: {self.expenses_dict}")

#GET MONTHLY CASH FLOW
    def cash_flow(self):
        print("\nFantastic, now we can get your monthly cashflow!")
        sleep(3)
        print("Drum roll please......")
        sleep(1)
        print("bttttttttt")
        sleep(1)
        print("bttttttttttt")
        sleep(3)
        print("btttttttttttttttt")
        sleep(4)

        income_values = []
        expense_values = []

        for value in self.income_dict.values():
            income_values.append(value)

        for value in self.expenses_dict.values():
            expense_values.append(value)

        income_result = sum(income_values)
        expense_result = sum(expense_values)

        cash_flow = income_result - expense_result
        print(f"Your monthly cash flow is ${cash_flow}")

#GET CASH ON CASH 
    def cash_on_cash(self):

        total_investment_list = []

        print("\nLet's get your cash on cash ROI\nAKA Total investment!")
        sleep(3)
        print("\nWhat was the total inital payments for the property?")
        
        while True:
            down_payment = input("What was the property's down payment: ")
            if down_payment.isnumeric():
                self.cash_roi_dict['down payment'] = int(down_payment)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")
        
        while True:
            closing_cost = input("What were the closing cost if any: ")
            if closing_cost.isnumeric():
                self.cash_roi_dict['closing cost'] = int(closing_cost)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")
        
        while True:
            repair_cost = input("What were the repairs needed at purchase: ")
            if repair_cost.isnumeric():
                self.cash_roi_dict['repair costs'] = int(repair_cost)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")

        while True:
            misc_cash_cash = input("Were there any miscellaneous costs at closing: ")
            if misc_cash_cash.isnumeric():
                self.cash_roi_dict['miscellaneous costs'] = int(misc_cash_cash)
                break
            else:
                print("I'm sorry, but this should be a number. \nPlease try again.")

        for value in self.cash_roi_dict.values():
            total_investment_list.append(value)

        self.total_investment = sum(total_investment_list)
        print(f"Your total investment is ${self.total_investment}")

#GET ANNUAL CASH FLOW
    def annual_cash_flow(self):
        annual_cash = []

        for value in self.income_dict.values():
            annual_cash.append(value)

        sum_annual_cash = sum(annual_cash)

        self.annual_income_result = sum_annual_cash * 12
        
        sleep(3)

        print(f"Your anuual cash flow is ${self.annual_income_result}")

# GET ANNUAL ROI FORMULA
    def annual_ROI(self):
        roi = self.annual_income_result / self.total_investment
        sleep(3)
        print(f"Your annual ROI is {roi:.2f}%")
    
    def get_roi(self):
        calc = Calulator()
        calc.get_income()
        calc.get_expenses()
        calc.cash_flow()
        calc.cash_on_cash()
        calc.annual_cash_flow()
        calc.annual_ROI()

calc = Calulator()
calc.get_roi()