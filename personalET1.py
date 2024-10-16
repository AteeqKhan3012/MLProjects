expenses = []

categories = set()

def expenses_data(expense_name, amount, category):
    attempt = 0
    while True:
        if attempt<3:
            expense_name = (input("Enter name of the expense: "))
            amount = int(input("Enter the amount of expense: "))
            category = input("Enter the expense category")

            expenses.append((expense_name, amount, category))

            categories.add(category)
            attempt+=1
        else:
            break        

expenses_data('expense_name', 'amount', 'category')   

print("Expenses logged in", expenses)

print("Categories:",categories)

summary = {category: sum(amount for expense_name, amount, cat in expenses if cat == category) for category in categories}

print("Expense summary by Category:",summary)


    