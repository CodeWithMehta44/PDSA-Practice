#Shuffle 
#M1
def shuffle(l1, l2):
    if len(l1)<len(l2):
        minlength = len(l1)
    else:                            #minlength= min(len(l1),len(l2))
        minlength = len(l2)
    shuffled = []
    for i in range(minlength):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    shuffled = shuffled +  l1[minlength:] + l2[minlength:]
    return(shuffled)
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5,6]
print(shuffle(l1,l2))

#M2
def shuffle(l1,l2):
    i=0
    shuffle=[]

    while i < len(l1) and i < len(l2):
        shuffle.append(l1[i])
        shuffle.append(l2[i])
        i+=1
    shuffle = shuffle + l1[i:]+ l2[i:]
    return shuffle
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5,6]
print(shuffle(l1,l2))

    