list_1=[1,2,3,4,5,6,7,8,9,10]
list_2=[2,5]
result=[]
result1=[]
for (i),val in enumerate(list_1):
    if val%2==0:
        k=list_2[(i // 2) % 2]
        result.append(val*k)
    else:
            k=list_2[(i // 2) % 2]
            result1.append(val*k)
print("Even numbers:", result)
print("Odd numbers:", result1)
            