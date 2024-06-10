#    BUILT IN DATA STRUCTURES

#list - sequential manner, indexed , negative index support , different data types , mutable

# l1 =[1,2,3,True,"Paras Dattera"] 
# print(l1)
# print(l1[3])
# print(type(l1))
# print(l1[0:5])
# l1[0]=2  
# print("mutated list is : ",l1)
# l1.append("Python")
# print("append is used to add element at at end of list, after adding element list is : ",l1)
# l1.append(["python","programming"])
# print(l1)
# l1.pop()
# a=list()
# a.append("python")
# print(a)
# b=list(range(1,10))
# print(b)
# b.insert(2,"new element")
# print(b)
# b.extend(range(2,6))
# print(b)
# b.extend(["new elements"])
# print(b)
# b.remove("new element")
# print(b)
# print(b.index(1))
# print(b.count(3))
# c=[1,2,3,7,5,4,8,5,23,65,21]
# c.sort()
# print(c)
# c.sort(reverse=True)
# print(c)
# c.reverse()
# print(c)
# new_list=c.copy()
# new_list1=list(c)
# print("new list copied from c is ",new_list," and ",new_list1)
# print(len(c))
# b.clear()
# print(b)
# d=["a","b","c","a"]
# d.sort()
# print(d)
# print("\n\n\n\n\n\n")

#dictionary - key value pairs , can be added , accessed and deleted as needed by keys

# d1 ={"Name":"Paras Dattera" , "Age":"22"}
# print(d1)
# print(d1.keys())
# print(d1.values())
# d1["Name"]="Charu Dattera"
# print(d1)
# print(type(d1))

#tuple - similar to list but immutable , indexed 

# t1 = (1,2,3,'Paras','Dattera')
# print(t1[3])
# print(t1[-1])
# print(type(t1))

# #set - collection of unordered unique elements , every element has to be unique

# s1={1,2,3,3,"new","newb","newc"}
# s1.add(25)
# s1.update(["A","B"])
# print(s1)
# print(type(s1))