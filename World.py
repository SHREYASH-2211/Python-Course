n=int(input("Enter number of person: "))

names=[]
salary=[]
for x in range(n): 
    name=input("Enter your name: ")
    salaries=int(input("Enter your salary: "))
    names.append(name)
    salary.append(salaries)

for i in range(n):
    print(f"\nName: {names[i]}")
    print(f"Salary: {salary[i]}")

for i in range(n):
    for j in range(0,n-i-1):
        if (salary[j]>salary[j+1]):

            temp=salary[j]
            salary[j]=salary[j+1]
            salary[j+1]=temp

            temp=names[j]
            names[j]=names[j+1]
            names[j+1]=temp

for i in range(n):
    print(f"\n Name: {names[i]} \tSalary: {salary[i]}")

