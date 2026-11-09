sum =0
a = ""
z=0
A = int(input("Enter a 1st: "))
B = int(input("Enter a 2nd: "))

if A>B:
    temp = A
    A = B
    B = temp

for i in range(A, B):
    j=1
    while j <= i:
        if i % j == 0:
            sum = sum + j
        j = j + 1
    if sum == i:
        z= z + 1
        a = a + str(i) + " "
        
        if z==0:
            print("Nqma perfekni chisla")
        else:
            print("Perfeknite chisla sa: ", a)