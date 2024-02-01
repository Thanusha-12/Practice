#WRITE operation

f = open("test for R&W", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("test for R&W", "r")
print(f.read())


# with open("test for R&W",'r') as reader:
#     content = reader.readlines()
#     reversed(content)
#     with open("test for R&W",'w') as writer:
#         for line in reversed(content):
#             writer.write(line)
