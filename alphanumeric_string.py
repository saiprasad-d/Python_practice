string= input('Enter the string: ')    # input string
lis=[i for i in string]   #extracting each element from string
num=['0','2','4','6','8']   #list of even numbers
count=0
#iterating through for loop for figuring out count of even numbers in the string
for i in lis:
    if i in num:
        count+=1
    else:
        continue
print('Total number of even number is: ',count)
