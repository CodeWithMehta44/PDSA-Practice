def factor(n):
    factorlist=[]
    for i in range(1, n+1):
        if n%i==0:
            factorlist.append(i)
    return(factorlist)

def isprime(n):
    return(factor(n)==[1,n])

def product_prime(n):
    for i in range(1, n+1):
        if n%i==0:
            if isprime(i) and isprime(n//i):
                print("The product is:",i,"X",n//i)
                return(True)
    return(False)
n= int(input("Enter the number:"))
print(product_prime(n))
print(factor(n))


