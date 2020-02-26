list1=list2=[]
list1=eval(input("enter the list: "))
for i in range(len(list1)):
    count=0
    for j in range(i):
        if list1[i]== list1[j]:
            count=1
    if count==1:
        continue
    else:
        list2.append(list1[i])
print(list2)


