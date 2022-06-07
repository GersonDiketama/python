

myfile = open("file-processing/files/fruits.txt")
print(myfile.read())

# this is if I want to read the content many times

file = open("file-processing/files/fruits.txt")
content = file.read()

print(content)
print(content)
print(content)


# better way to read file

with open("file-processing/files/fruits.txt") as myfiles:
    # this will read and close it
    contents = myfiles.read()

print(content)


# Writing into a file

with open("file-processing/files/vegetables.txt", "w") as writfile:
    cont = writfile.write("Tomato\nCucumber\nOnion\Gerson")

print(cont)


# copying 90 charathers from another file to past into different file.

with open("bear.txt") as myfile:
    content = myfile.read()
    chart = content[:90]
    with open("first.txt", "w") as newfile:
        cont = newfile.write(chart)


# Appending to exisiting text file

with open("file-processing/files/vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()

print(content)
