i=0
percent = 0
j=0
z=1
n = int(input("Enter a number: "))
if n == 0:
    print("Invalid number")
else:
    min = n

while n != 0:
    inital=n
    n = int(input("Enter a number: "))
    if n==0:
        break
    if n < min:
        min = n
    if n>inital:
        i = i+1
    if n<0:
        j= j+1
    z= z+1
        
percent = (j/(z))*100     
print("The smallest number is: ", min)
print("broq na narastvaniq e: ", i)
print("procent na otricatelni e: ", percent, "%")
    