from asyncore import read


myfile = open("fruits.txt")
print(myfile.read())

# this is if I want to read the content many times

file = open("fruits.txt")
content = file.read()

print(content)
print(content)
print(content)


# better way to read file

with open("fruits.txt") as myfiles:
    # this will read and close it
    contents = myfiles.read()

print(content)
