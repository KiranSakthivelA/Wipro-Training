# Count how many times A

text = input('Enter Your Text : ')
count = 0
for index, char in enumerate(text):
    if char.lower() == 'a':
        count +=1

print (count)