# with open("my_file.txt") as f:
#     contents = f.read()
#     print(contents)


with open("my_file.txt", mode = "a") as f: 
    f.write("\nNew Text.")
