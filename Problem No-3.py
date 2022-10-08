# Write a recursive python function to calculate sum of first N even natural numbers.
def function(a):
    if a==1:
        return(2*1)
    else:
        return((2*a)+function(a-1))
sum=function(int(input("Enter the value of n to calculate and print the sum of first n even natural numbers: ")))
print("Sum: ",sum)