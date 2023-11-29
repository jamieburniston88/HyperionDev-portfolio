num = 20
''' counts down from 20 - 0 in inclemants of 1'''
while num >= 0:
    print(num)
    num -= 1
''' uses the range of 0-22 and prints all even numbners'''
for num in range (22):
    if num % 2 == 0:
        print(num)
''' uses the range of 1-6 and prints '*' plus 1 each inclemant'''
for i in range(1,6):
    print('*'*i)