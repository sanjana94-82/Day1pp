#good pair values
def good_pair_values(a):
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                count+=1
    return count
l=[1,2,3,4,1,0,2]
print(good_pair_values(l))
