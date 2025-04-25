number = int(input())

for i in range(2, number):
    if number % i == 0:
        print('合成数です')
        break
else:
    print('素数です')
