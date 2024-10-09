string="hey buddy"
vowels=set()

for char in string:
    if char== 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'or \
       char== 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
          vowels.add(char)
print("vowels are these", vowels)   
