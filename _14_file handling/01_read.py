file = open("text.txt", "r")
content = file.read()
print(content)
file.close()

file = open("text2.txt", "w")
content = "This is new file"
file.write(content)
file.close()

