string2=""
string=input("Enter a sentence: ")
list1=string.split()
l=len(list1)
for i in range(l):
    string2=string2+list1.pop()+" "
print(string2)