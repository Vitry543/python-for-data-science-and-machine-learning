# create a function to calculate the factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input("enter the number: "))))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

def print_fact(n):
    result=fact(n)
    print(f"the factorial of {n} is {result}")

print_fact(int(input("enter the number: ")))
