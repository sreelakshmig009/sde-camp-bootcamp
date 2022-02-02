# check vowels
vowels = ['a','e','i','o','u']
flag = False
string = input()
for s in string:
  if s in vowels:
    flag = True
if flag == True:
  print("Contains vowels")
else:
  print("Doesnt contain vowels")
  
