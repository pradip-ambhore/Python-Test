file = open('test.txt')
#print(file.read(3))


# print(file.readline())
# print(file.readline())

# line = file.readline()
# while line !="":
#     print(line)
#     line=file.readline()

print("___________________________________________")

for line in file.readlines():
    print(line)
file.close()



