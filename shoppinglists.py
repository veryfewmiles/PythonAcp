shopping_list = {
"pen": 2,
"shovel": 1,
"body bag": 1,
"black mask": 2
}
myfile = open("shopping.txt","w")
for item, amount in shopping_list.items():
  myfile.write(item +":" + str(amount)+"\n")
myfile.close()
myfile = open("shopping.txt","r")
print(myfile.read())
myfile.close()