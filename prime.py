x=int(input("Enter your number:"))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("It is not a prime number")
            break
        else:
            print("It is a prime number")
            break
else:
    print("It is not a prime number")            







