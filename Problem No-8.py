# Write a recursive python function to print binary of a given decimal number.
def function(a):
    if a==0:
        print(0,end="")
    elif a==1:
        print(1,end="")
    else:
        function(int(a/2))
        print(int(a%2),end="")
n=int(input("Enter a number to calculate binary of given decimal number: "))
print(" Binary of given decimal number is : ",end=" ")
function(n)