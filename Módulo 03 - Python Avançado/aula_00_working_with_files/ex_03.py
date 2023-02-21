# Program to show various ways to
# read data from a file.
 
# Creating a file
file1 = open("ex_03.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes
 
file1 = open("ex_03.txt", "r+")
 
print("Output of Read function is ")
print(file1.read())
print()
 
# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)
 
print("Output of Readline function is ")
print(file1.readline())
print()
 
file1.seek(0)
 
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
 
file1.seek(0)
 
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
 
file1.seek(0)
 
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


"""
Output of Read function is 
Hello 
This is Delhi 
This is Paris 
This is London 


Output of Readline function is 
Hello 


Output of Read(9) function is 
Hello 
Th

Output of Readline(9) function is 
Hello 


Output of Readlines function is 
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n'] 
"""