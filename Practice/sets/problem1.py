total=int(input("Enter the total number you want to add in set"))

s=set()


for x in range(total):
    n=int(input(f"Enter number {x+1} :"))
    s.add(n)

print(s)