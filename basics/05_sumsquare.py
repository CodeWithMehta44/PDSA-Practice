#M1
def sumsquare(l):
    even=0
    odd=0
    for n in l:
        if n%2==0:
            even = even + n*n
        else:
            odd = odd+ n*n
    result = [odd,even]
    return result
l=[2,4,6]
print(sumsquare(l))
        
#M2
def sumsquare(l):
    odd=sum(n*n for n in l if n%2!=0)
    even=sum(n*n for n in l if n%2==0)
    return[odd,even]
l=[2,4,6]
print(sumsquare(l))