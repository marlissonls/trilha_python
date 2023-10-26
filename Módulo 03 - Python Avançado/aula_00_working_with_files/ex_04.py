
# Python program to illustrate
# Append vs write mode
file1 = open("ex_04.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
file1.writelines(L)
file1.close()
  
# Append-adds at last
file1 = open("ex_04.txt","a")#append mode
file1.write("Today \n")
file1.close()
  
file1 = open("ex_04.txt","r")
print("Output of Readlines after appending") 
print(file1.readlines())
print()
file1.close()
  
# Write-Overwrites
file1 = open("ex_04.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()
  
file1 = open("ex_04.txt","r")
print("Output of Readlines after writing") 
print(file1.readlines())
print()
file1.close()