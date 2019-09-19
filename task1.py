a=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']
nos=0
max=0
for i in a:
    if isinstance(i,list):
        nos+=1
        if max < len(i):
            max=len(i)
            index=a.index(i)
print("Length of above nested list:",len(a))
print("no of sublists present in tha nested list:",nos)
print("The sublist with the max length:",a[index])
print("The index of sublist with max length:",index)

