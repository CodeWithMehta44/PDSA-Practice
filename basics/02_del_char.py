#M1
def del_char(s,c):
    if len(c)!=1:
        return(s)
    snew=""
    for char in s:
        if char!=c:
            snew= snew + char
    return(snew)

s = input("Enter the word ")
c = input("Enter the letter")
print(del_char(s,c))

#M2
def del_char(s,c):
    if len(c)!=1:
        return s 
    return s.replace(c,"")
s = input("Enter the word ")
c = input("Enter the letter")
print(del_char(s,c))