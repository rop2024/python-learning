try:
    x = 2/0
    raise Exception("Haha error")
except:
    print("Some error occured")
else:
    print("No error occured")

finally:
    print("Program executed successfully")