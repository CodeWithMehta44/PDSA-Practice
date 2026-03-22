def build_table(l):
    frequency= {}
    for n in l:
        if n in frequency.keys():
            frequency[n]=frequency[n]+1
        else:
            frequency[n]-1
    return (frequency)

def sort_table(fdict):
    flist = [(fdict[n], n) for n in fdict.keys()]
    flist.sort()
    return([(n,r) for (r,n) in flist])
def histogram(l):
    freq_table = build_table(l)
    return(sort_table(freq_table))
l=eval(input())
print(histogram(l))