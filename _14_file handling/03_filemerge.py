file1 = open("text3.txt", "w")
file1.write("This is new file lets write something in this")
file1.close()

file2 = open("text2.txt", "a")
file1 = open("text3.txt", "r")

content = file1.read()
file2.write(f"\n{content}")

file2.close()
file1.close()