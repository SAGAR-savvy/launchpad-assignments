##list1=list()
list2= list()
list1=eval(input("enter the list elements: "))
ele= int(input("enter the element to be searched: "))
for i in range(len(list1)):
    if(list1[i]==ele):
        list2.append(i)
    i=i+1
print(list2)