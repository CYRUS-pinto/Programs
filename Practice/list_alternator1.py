list_1=[1,2,3,4,5,6,7,8,9,10]
list_2=[2,5,10]
#list=[list_1[i] for i in range(1,len(list_1),2)]
#new_list=[list_1[i] for i in range(1,len(list_1),2)]
#list=[value*list_2[index%3] for index,value in enumerate(list)]
#print ([value*list_2[index%(len(list_2))] for index,value in enumerate(list)])
print ([value*list_2[i%(len(list_2))] for i,value in enumerate(list_1[2::3])])