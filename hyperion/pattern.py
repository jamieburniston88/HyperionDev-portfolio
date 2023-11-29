'''Uses the range()to check if number is less or equal to 5,
if true it prints '*' multiplied by i, otherwise it prints '*'
multiplied by (10 - i).'''

for i in range(1,10):
    if i <= 5:
        print('*'*i)
    else:
        print('*'*(10 - i))