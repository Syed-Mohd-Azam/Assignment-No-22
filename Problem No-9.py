# Write a recursive python function to print octal of a given decimal number.
def function(a):
    if a in(0,1,2,3,4,5,6,7):
        print(a,end="")
    else:
        function(int(a/8))
        print(int(a%8),end="")
n=int(input("Enter the decimal number to calculate its octal equivalent: "))
print("Octal Equivalent of given decimal number is : ",end=" ")
function(n)