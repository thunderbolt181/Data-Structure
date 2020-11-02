l,c=list(map(int,input("Enter the elements\n=>").split())),True
s=int(input("Enter the search element =>\t"))
first,last=0,len(l)-1
while(first<=last):
	mid = (first + last)//2
	if (l[mid] == s):
		print("Search element {0} is in index no. {1}".format(s,mid+1))
		c=False
		break
	else:
		if s < l[mid]:
			last = mid - 1
		else:
			first = mid + 1
if c==True:
	print("Search element {0} not found".format(s))