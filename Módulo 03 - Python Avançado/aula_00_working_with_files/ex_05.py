# Program to show various ways to
# read data from a file.
 
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Creating a file
with open("ex_04.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes
 
with open("ex_04.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())