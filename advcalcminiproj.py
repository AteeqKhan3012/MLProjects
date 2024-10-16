def adv_calc():
    while True:
        print("Advance Calculator Operations")
        print("Select 1 for Addition")
        print("Select 2 for Subtraction")
        print("Select 3 for multiplication")
        print("Select 4 for division")
        try:
            Choose=int(input("Choose the number to select the operation"))
            a=int(input("Enter the a value of a: "))
            b=int(input("Enter the b value of b: "))
            try:
                if Choose == 1:
                    c=a+b
                    print("The addition of a&b is:",c)
                elif Choose == 2:
                    c=a-b
                    print("The subtraction of a&b is:",c)
                elif Choose == 3:
                    c=a*b
                    print("The multiplication of a*b is:",c)
                elif Choose == 4:
                    c=a/b
                    print("The division of a/b is:",c)
                else:
                    print("Invalid operation")
            except Exception as e:
                print(e)
            print("Select 5 to continue the operation again or 0 to exit")
            Choose1=int(input("Enter 5 to continue the operation or 0 to exit"))
            if Choose1 == 5:
                        continue
            elif Choose1 == 0:
                        break
            else:
                print("Invalid operation")
        except Exception as e:
            print(e)

adv_calc()
          