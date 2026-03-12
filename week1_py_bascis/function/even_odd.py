def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

def print_even_odd(n):
    result=even_odd(n)
    print(f"the number {n} is {result}")

print_even_odd(int(input("enter the number: ")))