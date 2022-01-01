def chargingphone(inicharge, finalcharge):
    current = inicharge
    time_taken = 0
    while current <= finalcharge:
        if 0 <= current <= 10:
            current = current + 10
            time_taken +=1
        elif 11 <= current <= 230:
            current = current + 5
            time_taken +=1
        elif 231 <= current <= 559:
            current = current + 8
            time_taken +=1
        elif 560 <= current <= 1009:
            current = current + 2
            time_taken +=1
        elif 1010 <= current <= 5000:
            current = current + 7
            time_taken +=1
        elif 5001 <= current <= 10000:
            current = current + 8
            time_taken +=1
        elif 10001 <= current <= 10**9:
            current = current + 3
            time_taken +=1
    return time_taken

inicharge=int(input('Enter value of current charge: '))
finalcharge=int(input('Enter level of final charge required: '))
print('Time taken by smart charger to charge a phone is ',chargingphone(inicharge,finalcharge))
