import math

class Category:
    
    def __init__(self, category, ledger=[]):
        self.category = category
        self.ledger = []
        self.deposits = 0
        self.withdrawals = 0
    
    def deposit(self, amount, description=""):
        self.deposits += amount
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, withDrawAmount, description=""):
        if withDrawAmount < self.deposits:
            self.ledger.append({"amount": -withDrawAmount, "description": description})
            self.withdrawals += withDrawAmount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.deposits - self.withdrawals

    def transfer(self, amount, category):
        if amount < self.deposits:
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False
    
    def __str__(self):
        length_top = 30 - len(self.category)
        budgetString = "*" * (length_top//2) + self.category + "*" * (length_top//2) + "\n"
        for item in self.ledger:
            length = 30 - len(item["description"][:23])
            budgetString += item["description"][:23] + " "  + str(format(item["amount"], '.2f')).rjust(length - 1) + "\n"
        budgetString += "Total:" + " " + str(format(self.get_balance(), '.2f'))
        return budgetString



def create_spend_chart(categories):

    line_100 = "100|"
    line_90 = " 90|"
    line_80 = " 80|"
    line_70 = " 70|"
    line_60 = " 60|"
    line_50 = " 50|"
    line_40 = " 40|"
    line_30 = " 30|"
    line_20 = " 20|"
    line_10 = " 10|"
    line_0 = "  0|"
    

    spenses = {}
    names = []
    Total = 0

    for item in categories:
        Total += item.withdrawals
        spenses[item.category] = item.withdrawals
        names.append(item.category)
    
    for amount in spenses.values():
        percentage = ((amount/Total) * 100)

        remainder = percentage % 10
        if remainder < 5:
            percentage = int(percentage / 10) * 10
        else:
            percentage = int((percentage + 10) / 10) * 10
        
        #print(category, percentage)
        if percentage == 100:
            line_100 += " o"
            line_90 += " o"
            line_80 += " o"
            line_70 += " o"
            line_60 += " o"
            line_50 += " o"
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=90 and percentage < 100:
            line_90 += " o"
            line_80 += " o"
            line_70 += " o"
            line_60 += " o"
            line_50 += " o"
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=80 and percentage < 90:
            line_80 += " o"
            line_70 += " o"
            line_60 += " o"
            line_50 += " o"
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=70 and percentage < 80:
            line_70 += " o"
            line_60 += " o"
            line_50 += " o"
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=60 and percentage < 70:
            line_60 += " o"
            line_50 += " o"
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=50 and percentage < 60:
            line_50 += " o"
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=40 and percentage < 50:
            line_40 += " o"
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=30 and percentage <40:
            line_30 += " o"
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=20 and percentage <30:
            line_20 += " o"
            line_10 += " o"
            line_0 += " o"
        elif percentage >=10 and percentage <20:
            line_10 += " o"
            line_0 += " o"
        elif percentage >=0 and percentage <10:
            line_0 += " o"
    
    maxLength = max(names, key=len)

    x_axis = ""

    for x in range(len(maxLength)):
        nameStr = '     '
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        nameStr += '\n'
        x_axis += nameStr
        
    #print(x_axis)
    
    dashes = '-' * (len(line_0) - 2)
    chart = "Percentage spent by category"
    chart += '\n' + line_100 + '\n' + line_90 + '\n' + line_80 + '\n' + line_70 + '\n' + line_60 + '\n' + line_50 + '\n' + line_40 + '\n' + line_30 + '\n' + line_20 + '\n' + line_10 + '\n' + line_0 + '\n' + '    ' +  dashes
    chart +=  '\n' + x_axis   

    return chart

food = Category("Food")
food.deposit(1000, 'initial deposit')
# print(food.ledger[0])
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.ledger)
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
# print(clothing.ledger)
# print(food.ledger)
# print(food.get_balance())
# print(food.check_funds(1000))
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food.withdrawals)
# print(clothing.withdrawals)
# print(auto.withdrawals)

print(create_spend_chart([food, clothing, auto]))