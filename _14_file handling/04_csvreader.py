import csv

rows = []
file = open("sample.csv", "r")
csv_read = csv.reader(file)

fields = next(file)
print(fields)

for row in file:
    rows.append(row)



print("rows are: ")
for row in rows:
    print(row)

file.close()