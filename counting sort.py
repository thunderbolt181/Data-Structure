def counting_sort(a):
    temp_a=[0]*(max(a)+1)
    for i in a:
        temp_a[i]+=1
    for i in range(1,len(temp_a)):
        temp_a[i]+=temp_a[i-1]
    sorted_arr=[None]*(len(a))
    for i in range(len(a)-1,-1,-1):
        sorted_arr[temp_a[a[i]]-1] = a[i]
        temp_a[a[i]]-=1
    print(sorted_arr)

a=[4,2,2,8,3,3,1]
counting_sort(a)