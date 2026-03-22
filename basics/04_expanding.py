#Iterator Method 
def expanding(l):
    if len(l)<=2:
        return True
    olddiff = abs(l[0]-l[1])
    for i in range(2,len(l)):
        newdiff = abs(l[i]-l[i-1])
        if olddiff>=newdiff:
            return False
        olddiff = newdiff
    return True
l=[1,3,6,10,15,27]
print(expanding(l))


#Recurssive Method  
def expanding(l):
    if len(l)<=2:
        return True
    diff = abs(l[0]-l[1])
    return(diff<abs(l[1]-l[2]) and expanding(l[1:]))  
l=[1,3,6,10,15,27]
print(expanding(l))