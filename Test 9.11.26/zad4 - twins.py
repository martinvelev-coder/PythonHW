prosto = True
n = int(input("Enter a number: "))
while n<5:
    inital = n
    n = int(input("Enter a number: "))
    if inital == n + 2 or inital == n - 2:
        print("The numbers are twins: " ,inital, "and", n)
    for i in range(2, **n):
        if n % i == 0:
            prosto = False
            break