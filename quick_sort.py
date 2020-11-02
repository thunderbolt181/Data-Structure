def partition(a,s,e):
    i,j=s,s
    while(j<e):
        if a[j]<a[e]:
            a[j],a[i] = a[i],a[j]
            i+=1
            j+=1
        elif a[j]==a[e] or a[j]>a[e]:
            j+=1
    a[i],a[e]=a[e],a[i]
    return i

def quicksort(a,s,e):
    if s<e:
        i = partition(a,s,e)
        quicksort(a,s,i-1)
        quicksort(a,i+1,e)

a=[2,8,7,1,3,5,6,4,415,654,2332,3,65,3,32]
quicksort(a,0,len(a)-1)
print(a)