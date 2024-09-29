question=input("Do You Want to book a slot: ").upper()

if("YES" in question):
        
        name=input("\nEnter you name: ").upper()

        print("\n\nEnter the date and in this format \nDD for Date then press enter key then enter MM for month")

        date=int(input("DATE: "))
        month=int(input("MONTH: "))

        type=(f"\n\n\nThank you {name} your slot has been book on {date}/{month}/2024\n\n").upper()
        print(type)

else:
        print("Thank You")



    