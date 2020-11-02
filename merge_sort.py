def merge(a,b,c):
    i=j=k=0
    while i<len(b) and j<len(c):
        if b[i] < c[j]:
            a[k]=b[i]
            i+=1
        else:
            a[k]=c[j]
            j+=1
        k+=1
    while i<len(b):
        a[k]=b[i]
        i+=1
        k+=1
    while j<len(c):
        a[k]=c[j]
        j+=1
        k+=1

def m_sort(a):
    if len(a)>1:
        m = len(a)//2
        b = a[:m]
        c = a[m:]
        m_sort(b)
        m_sort(c)
        merge(a,b,c)

a=[5,4,3,6,8,7,9,5,2,1]
m_sort(a)
print(a)