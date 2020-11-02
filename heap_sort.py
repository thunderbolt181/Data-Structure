def heapify(a,c):
    b=False
    d=(c//2)-1
    for i in range(d,-1,-1):
        j,k=(2*i)+1,(2*i)+2
        if c-1 >= k:
            if a[j] > a[i] or a[k] > a[i]:
                if a[j] > a[k]:
                    a[j],a[i] = a[i],a[j]
                    b=True
                else:
                    a[k],a[i] = a[i],a[k]
                    b=True
        else:
            if a[j] > a[i]:
                a[j],a[i] = a[i],a[j]
                b=True
    if b:
        heapify(a,c)

def heap_sort(a):
    for i in range(len(a)-1,-1,-1):
        heapify(a,i+1)
        a[0],a[i]=a[i],a[0]

a=[2,2,4,6,34,23,4,54,2,1,43,6,8,5]
heap_sort(a)
print(a)