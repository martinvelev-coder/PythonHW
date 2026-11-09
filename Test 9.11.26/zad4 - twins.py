prosto = True
n = int(input("Enter a number: "))
while n<5:
    n = int(input("Enter a number: "))
    for i in range(2, **n):
        if n % i == 0:
            prosto = False
            break