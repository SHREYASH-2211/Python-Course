item=int(input("How many items: "))
names=[]
#prices=[]
total=0
for x in range(item):
    name=input(f"Enter item {x+1}: ")
    names.append(name)
    price=int(input(f"Enter amount for {name}: "))
    #prices.append(price)
    total+=price

for name in names:
    print(name)
print(f"Your total amount is {total}\n\n")

ans=input("Do you want to purchase: ").upper()

if(ans=="YES"):
    store=input("How would you like to pay Cash or Card: ").upper()
    if(store=="CASH"):
        print("Thank you \n Visit again")
    elif(store=="CARD"):
        name=input("Enter your name: ")
        while (True):
            creditnumber = input("\nEnter 12 digit number: ")
            if len(creditnumber) == 12 and creditnumber.isdigit():
                creditnumber = int(creditnumber)  # Convert to int after validation
                break
            else:
                print("Invalid input. Please enter exactly 12 digits.")
        print("Enter expiry date in this format DD/MM/YYYY")
        d=int(input())
        m=int(input())
        y=int(input())
        balance=int(input("Enter Your Balance"))
        print("\n\nUser Informaton:")
        print(f"Name: {name}\nCredit number: {creditnumber}\nExpiry: {d}/{m}/{y}\n") 
        if(balance>total):
            balance-=total
            print(f"Remaining balance in your account: {balance}")
            print("Thank you Visit again")
        else:
            print(f"Not have enough balance\nRemaing balance: {balance}\n")
            exit(0)
    else:
        print("Invalid payment method.")
else:
    print("Thank you Visit again")
    exit(0)