N = int(input("Enter a number: "))
sum =0
i = 0
j=0
if N <= 0:
    print("Invalid number")
while N>0:
    n = int(input("Enter a number: "))
    if n%3 == 0:
        i = i+1
    N = N-1
    if n >= 0:
        sum =sum + n
        j = j+1
sum = sum/j
print("Broq chisla kratni na 3: ", i)
if j==0:
    print("Nqma polovitelni")
else:
    print("Sredno", sum)


    

