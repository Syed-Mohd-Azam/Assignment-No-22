# Write a recursive python function to calculate sum of first N odd natural numbers.
def function(a):
    if a==1:
        return(2*1-1)
    else:
        return((2*a-1)+function(a-1))
sum=function(int(input("Enter the value of n to calculate the sum of first n odd natural numbers:  ")))
print("sum: ",sum)