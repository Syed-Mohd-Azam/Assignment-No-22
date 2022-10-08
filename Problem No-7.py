# Write a recursive python function to calculate sum of the digits of a given number.
def function(num):
    if num==0:
        return(0)
    else:
       return (int(num%10)+function(int(num/10)))
sum=function(int(input("Enter a number to calculate the sum of digits of a given number: ")))
print("Sum : ",sum)