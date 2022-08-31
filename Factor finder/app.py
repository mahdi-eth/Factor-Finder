def factor_finder(n):
    for i in range(1,n+1):
        if n % i == 0: print(i)

n = int(input("Enter any number to see it's factors : "))
factor_finder(n)