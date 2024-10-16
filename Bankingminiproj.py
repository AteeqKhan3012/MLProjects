Account_Bal=1000
def check_balance():

  
  while True:
    print("Welcome to banking")  
    print("Press 0 - to view your balance \nPress 1 - to deposit \nPress 2 - to withdraw \nPress 3 - to exit")
    choice = int(input("Enter your choice: "))
    if choice == 0:
          Account_Balance()
    elif choice == 1:
          deposit()
    elif choice ==2:
          withdraw()
    elif choice == 3:
          print("Exiting the program")
          break
    else:
          print("You have made an incorrect choice")
                           
def Account_Balance():
    
    print("Your balance is:",Account_Bal)  
def deposit():
        global Account_Bal
        amount = float(input("Enter the amount you want to deposit: "))
        Account_Bal += amount
        print(f"Your new balance is: {Account_Bal}")
def withdraw():
            global Account_Bal
            amount = float(input("Enter the amount you want to withdraw: "))
            if amount >  Account_Bal:
                print("Insufficient  balance!")
            elif  amount <= 0:
                print("Invalid amount!")
            else:
                Account_Bal -= amount
                print(f"Your remaining balance is: {Account_Bal}")
            
check_balance()