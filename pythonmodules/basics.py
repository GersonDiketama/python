import time
import os
import pandas


# Standard Python Modules
# this while loop won't work because of the first while loop

def loop():
    while True:
        if os.path.exists("pythonmodules/files/fruits.txt"):
            with open("pythonmodules/files/fruits.txt", "w") as myfruits:
                myfruits.write("Banana\n")
        else:
            print("No file found!")
        time.sleep(3)
        break


loop()


# Third party Modules

while True:
    if os.path.exists("pythonmodules/files/temps_today.cvs"):
        data = pandas.read_csv("pythonmodules/files/temps_today.cvs")
        print(data.mean())
    else:
        print("No file found!")

    time.sleep(3)
    break


while True:
    with open("pythonmodules/files/tomato.txt", "a+") as contfile:
        contfile.write("Write new line every 2 seconds\n")
        contfile.seek(0)
        print(contfile.read())
        # this will write and print every 2 seconds
        time.sleep(2)
