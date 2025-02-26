#remove duplicates
def remove_duplicates(a):
    nl=[]
    for i in a:
        if i not in nl:
            nl.append(i)
    return nl
l=[1,4,5,2,1,7]
print(remove_duplicates(l))
