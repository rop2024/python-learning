def create(dict, key, value):
    return dict.update({key:value})

def main():
    dictionary = {} # empty dict created
    create(dictionary, "name", "rohit")
    create(dictionary, "age", "19")
    create(dictionary, "hobby",["programming","blender"])

    print(dictionary)
    print(dictionary.keys())
    print(dictionary.values())
    print(dictionary.items())

if __name__ == "__main__":
    main()