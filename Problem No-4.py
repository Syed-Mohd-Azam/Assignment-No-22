# Write a recursive python function to calculate sum of squares of first N natural numbers.
def function(a):
    if a==1:
        return(1*1)
    else:
        return((a*a)+function(a-1))
sum=function(int(input("Enter the value of n to calculate the sum of squares of first n natural numbers: ")))
print("Sum: ",sum)