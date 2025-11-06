new_list=[1,2,3,4,5,6,7,8,9]
new_list.append(10)
print(new_list)
new_list.reverse()
print(new_list)
new_list.extend([3,5,6,7])
print(new_list)
new_list.sort()
print(new_list)
new_list.pop()
print(new_list)
new_list.remove(1)
print(new_list)
x=len(new_list)
print(x)


m="m"
str="a"
name="m"+str
str.upper()
print(str)
n=str+m
string="Mandar patil"
print(string.strip())
print(string.upper())
print(string.lower())
print(string.find("M"))
print(string.split())
print(string.replace("m","n"))
string.join(str)




roll ={1,2,3,3,4,4,5,5,6,546,454}
no={1000,200,23132,2123.21}
print(roll)

roll.add(453)
print(roll)
roll.union(no)
print(roll)
roll.remove(3)
print(roll)
roll.pop()
print(roll)
roll.discard(29380174)
print(roll)
roll.clear()
print(roll)



my_dict={"name":"mandar","roll":67,"department":"CSE"}
print(my_dict["name"])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.__len__())



my_tuple=(1,2,3,4,5,6)
print(my_tuple[1:4])
my_tuple2=(123,23,3333)
my_tuple3=my_tuple+my_tuple2
print(my_tuple3)
