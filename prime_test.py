number = int(input())

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print('合成数です')
        break
else:
    print('素数です')
