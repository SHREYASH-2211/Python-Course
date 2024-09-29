# Week Switch Case

choice=("Enter \n1 for Monday\n2 for Tuesday \n3 for Wednesday \n4 for Thrusday \n5 for Friday \n6 for Saturday \n7 for Sunday")

while(choice<0 or choice!>7):
    if(choice==1):
        print("Monday")
    if(choice==2):
        print("Tuesday")
    if(choice==3):
        print("Wednesday")
    if(choice==4):
        print("Thrusday")
    if(choice==5):
        print("Friday")
    if(choice==6):
        print("Saturday")
    if(choice==7):
        print("Sunday")
    else:
        print("Invalid Input")
