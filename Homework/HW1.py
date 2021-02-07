NumList = []
 
Number = int(input("How many elements in list :- "))
 
# condition to check given number is even or odd

 
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element :- " %i))
    NumList.append(value)
if( Number%2 == 0 ):
    
# divide by 2 the length of list 
  n = int(Number/2)
     
# Create list1 with half elements (first 3 elements)
  list1 = NumList [0:n]
# Create list2 with next half elements (next 3 elements)
  list2 = NumList [n:Number]
 
# print list (s)
  print("list : ",NumList)
  print("list1: ",list1)
  print("list2: ",list2)

  list3 = list2 + list1
  print(list3)

else:
  for i in range(len(NumList)//2):
    temp=NumList[i]
    NumList[i]=NumList[len(NumList)//2+1+i]
    NumList[len(NumList)//2+1+i]=temp
print(NumList)
