def factorial(n):
    if n>1:
        return n*factorial(n-1)
    elif n==1 or n==0:
        return 1
    else:
        raise Exception


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6