f = open("/Users/shreyashsingh/Documents/Code/Python-Course/file handling case/timepass.txt", "a")
f.write("\nHow are you")
f.close()

f = open("/Users/shreyashsingh/Documents/Code/Python-Course/file handling case/timepass.txt", "r")
print(f.read())
