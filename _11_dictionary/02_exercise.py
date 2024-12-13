def main():
    # create an empty dictionary called dog
    dog = {}
    # key_lists = ["name", "color", "breed", "legs", "age"]

    # for i in key_lists:
    #     dog[i] = None
    # empty list created

    # print(dog)

    # adding items in dict
    dog_list=[{"name":"Bulldog", "color":"white","breed":"British","legs":4, "age":3},{"name":"German Shepherd", "color":"Brown","breed":"German", "legs": 4,"age":5}]
    for dogs in dog_list:
        dog[dogs["name"]] = dogs

    # print(dog)
    print(dog.keys())
    print(dog.values())

    for dog_name, dog_info in dog.items():
        print(f"{dog_name}'s age is {dog_info["age"]}")
if __name__ == "__main__":
    main()