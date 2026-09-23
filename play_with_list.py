oringal_list=[1,2,3,4,5,6,7,8,9,10]

count=0

for i in oringal_list:
    count+=1
average=sum(oringal_list)/count

sum=sum(oringal_list)

print("Average of the list is:",average)
print("Sum of the list is:",sum)

oringal_list.sort()
print("the largest number in the list is:",oringal_list[-1])
print("the smallest number in the list is:",oringal_list[0])