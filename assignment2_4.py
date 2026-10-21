##file read

with open("student.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content, end="")
