with open("student.txt", "w") as file:
    file.write(str(input("enter the text to be displayed in the file:")))
    file.write("\nThis is a student grades file.")

print("Content written to file successfully!")