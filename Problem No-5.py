# Write a recursive python function to calculate sum of cubes of first N natural numbers.
def function(a):
    if a==1:
        return(1)
    else:
        return((a*a*a)+function(a-1))
sum=function(int(input("Enter the value of n to calculate the sum of cubes of first n natural numbers: ")))
print("Sum :",sum)