list =[10,20,30,44,67,]
print ("before swapping",list)
temp=0
if len(list) >1:
    temp=list[0]
    list[0]=list[-1]
    list[-1]=temp

print("after swapping",list)
         
