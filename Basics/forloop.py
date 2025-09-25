succesfull = True

for number in range(1, 11):
    print('Attempt', number, (number * '.') )
    if succesfull:
        print('succesfull')
        break
else:
    print('Attempted 10 times and failed')