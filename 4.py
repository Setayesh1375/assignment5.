list = []
number = int(input(" tedad adad list "))
i=0
for  i in range(number):
  x = int (input("adad ra vared konid " ))
  list.append(x)
  i+=1
print("list = " , list)


reverse_list = []

for i in range(len(list),0, -1):
    reverse_list.append(list[i-1])
 
print("reverse_list = " , reverse_list)
