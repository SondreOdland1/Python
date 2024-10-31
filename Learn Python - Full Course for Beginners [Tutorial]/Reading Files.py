
text_file = open('file.txt', 'r')
for text in text_file.readlines():
    print(text)



print(text_file.readable())
print(text_file.read())
print(text_file.readline())
print(text_file.readlines())
print(text_file.readlines()[1])



text_file.close()




