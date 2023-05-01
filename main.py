
import sys
array = [[1,2,2,2,3],[5,4,3,2,3],[3,3,3,6,5]]
biggercount = 1
count = 1
addressbegin = 0

the_number = 0
the_index= 0
curnum = sys.maxsize
for arr in array:
  for num in arr:
    if num == curnum:
      count +=1
      addressbegin=arr.index(curnum)
      the_number= num
        
    else: 
      if count>biggercount:
        biggercount=count
        the_index = addressbegin
        the_number=the_number
        print("Number:",the_number,biggercount)
        print("Address_begin:",the_index)
      count=1
    # print(num,end = ",")
    curnum = num
    
    
    
  print("\n")
#--reimplement
#--much better implementation for the address finding mechanism
array = [[1,2,2,2,3],[5,4,3,2,3],[3,3,3,6,5]]
biggercount = 1
count = 1
addressbegin = 0
no_update=0
the_number = 0
the_index= 0
curnum = sys.maxsize
for i in range(len(array)):
  for num in range(len(array[i])):
    #if array[i][num]
    if array[i][num]== curnum and num==0 and array[i-1][-1]==curnum:
      count+=1
      the_address = len(array[i])-1
      the_number=curnum
      no_update=1
    elif array[i][num] ==curnum and num!=0:
      count+=1
      if not no_update:the_address = array[i].index(curnum)
      the_number =curnum
    else:
      if count>biggercount:
        biggercount=count
        the_index=the_address
        the_number=the_number
        print("2.Number:",the_number,biggercount)
        print("2.Address_begin:",the_index)
      count=1
      no_update=0
    curnum=array[i][num]
  print("\n")  
        
      
