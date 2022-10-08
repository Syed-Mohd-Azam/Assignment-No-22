# Write a recursive python function to find the Nth term of the Fibonacci series.
def function(a,b,c):
    if c<=0:
        return()
    else:
        f,l=a,b
        s=a+b
        d=c-1
        print(s,end=" ")
        function(l,s,d)
n=int(input("Enter how mny terms you want to print of fibonacci series: "))
print("Fibonacci series: ",end=" ")
print(0,1,end=" ")
function(0,1,n-2)