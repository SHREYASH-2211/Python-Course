balance=int(input("Enter Your Balance: "))
total=0
choice=0
while(choice!=3 and choice<3):
    choice=int(input("Enter \n1 for Credit\n2 for Deposit\n3 for exit\n"))
    if(choice==1):
        total=int(input("Enter amount to be credited: "))
        balance+=total
        print(f"Total Balance: {balance}")
    elif(choice==2):
        total=int(input("Enter amount to be debited: "))
        balance-=total
        print(f"Total Balance: {balance}")
    elif(choice==3):
        print("Thank you")
        exit(0)
    else:
        print("Invalid choice")
    

