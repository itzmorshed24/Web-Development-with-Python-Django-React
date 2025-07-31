my_list = ["Dhaka", "Rangpur", "Dinajpur", "Bogura"]
print(my_list)

#Access Items
print(my_list[0])
print(my_list[-1])

#Change Item
my_list[2] = "Rajshahi"
print(my_list)

#Add Items
my_list.append("Thakurgoan")
my_list.insert(0, "Chirirbandar")
print(my_list)

#Remove Items
my_list.remove("Bogura")
my_list.pop()
del my_list[1]
print(my_list)

#List Length
print(len(my_list))
