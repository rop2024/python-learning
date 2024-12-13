from random import randint

# random_value = random.randint(1, 11)
# print(random_value)

subjects = [ 'dbms', 'maths']
modules = [1,2,3,4,5]
dict = {}

num = int(input("How many modules you would like to cover ? "))

while True:

    if len(dict) == num:
        print("Confirmation...")
        print(dict)

        confirm = input("Would this work ? ").lower()

        if confirm in ['yes', 'y', 'ha', 'ya', 'okay', 'ok']:
            break
        else:
            dict = {}

    else:
        random_subject = randint(0, len(subjects)-1)
        random_module = randint(0, len(modules)-1)

        dict[subjects[random_subject]] = modules[random_module]


sample_size = len(dict)
module_subpart = [1,2,3,4]

order = []

total = sample_size * len(module_subpart)

while len(order) < total:
    value = randint(1, total)
    if value not in order:
        order.append(value)

print(order)

# for i range(total):
#     if order

# upgraded version would have file handling feature
# file with all the modules that are completed
# file with frequency of topic coverage