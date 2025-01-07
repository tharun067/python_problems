
def sum(n):
    total=0
    for i in range(n):
        if i%2==0:
            total+=i
    return total
n=int(input("Enter the input value: "))
print("The sum of n even numbers: ",sum(n))