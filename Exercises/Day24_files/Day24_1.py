'''file = open('file')
contents = file.read()
print(contents)
file.close()'''

with open('file', mode='w') as file:
    file.write(" i'm to happy to be here")
    print()