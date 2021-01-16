list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6] 
list3 = []
def addTwoList():
    print('Adding elements inside list')
    for i in range(len(list1)):   
        list3.append(list1[i]+list2[i])
    print(list3)
    print('Another(zip) method to add list')
    for j in zip(list1, list2):
        print(sum(j), end=" ")
addTwoList()
