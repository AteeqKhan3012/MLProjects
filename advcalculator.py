def calc():
    while True:
        print(" choose which operation to be done by selecting the nums from 1 to 4")
        print(" select 1 for addition")
        print(" select 2 for substraction")
        print(" select 3 for multiplication")
        print(" select 4 for divison")
        try:
            select = int( input(" select the operation by giving valuable input"))
            a = int(input( " enter value for a "))
            b = int(input(" enter value for b "))
            try:
                if select == 1:
                    c = a+b
                    print(" addition",c)
                elif select == 2:
                    c = a-b
                    print(" sub",c)
                elif select ==3:
                    c = a*b
                    print(" mul",c) 
                elif select == 4:
                    c= a/b
                    print(" div",c)
                else:
                    print(" invalid input")
            except Exception as e:
                print(e)
            #break
            print(" press 9  to continue and 0 for exit")
            select2 = int(input(" select either 9 or 0 to continue or exit "))
            if select2 == 9:
                continue
            elif select2 == 0:
                break
            else:
                print(" invalid number")
        except Exception as e:
            print(e)
calc()