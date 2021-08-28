#Accept two numbers from the user and find output their sum in the given format
s=input("Enter 2 no.s : ")
ls=s.split()
sum=0
for i in ls:
     sum+=int(i)
print(sum)
