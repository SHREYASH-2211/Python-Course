def my_func(n):
    return lambda a:a*n
    

doubler=my_func(2)
tripler=my_func(3)

print(doubler(11))
print(tripler(11))
