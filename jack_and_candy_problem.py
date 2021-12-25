import math
while True:
    try:
        num = int(input('Enter the number of candies: ')) #input total count of candies
        break
    except:
        print('Enter valid input')

count=0
lis = [] #create list of candies 
        
#input types of candies
while count < num:
    typ = int(input())
    count=count+1
    lis.append(typ)
lis.sort() #sort the list

#calculating number of individual type of candies
frequencies = {}
for item in lis:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1

#calculating number of days
days=0
for value in frequencies.values():
    day1 = math.floor(value/2)  #rounding off to lower value
    day2 = value % 2
    day3 = day1 + day2
    days = days + day3   #summing up total days
print('Total number of days jack will take to finsih candies ',days)
