# Write a recursive python function to calculate the factorial of a number.
def function(a):
    if a==1:
        return(1)
    else:
        return(a*function(a-1))
fact=function(int(input("Enter a number to calculate its factorial: ")))
print("Factorial :",fact)