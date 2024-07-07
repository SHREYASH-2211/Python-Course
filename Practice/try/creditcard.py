name=input("Enter your name: ")
while True:
    creditnumber = input("\nEnter 12 digit number: ")
    if len(creditnumber) == 12 and creditnumber.isdigit():
        creditnumber = int(creditnumber)  # Convert to int after validation
        break
    else:
        print("Invalid input. Please enter exactly 16 digits.")
print("Enter expiry date in this format DD/MM/YYYY")
d=int(input())
m=int(input())
y=int(input())

print("\n\nUser Informaton:")
print(f"Name: {name}\nCredit number: {creditnumber}\nExpiry: {d}/{m}/{y}\n")

