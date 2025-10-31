# Open a file named "example.txt" in write mode ('w') and write to it
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")

# Open the file in read mode ('r') and print its content
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Open the file in append mode ('a') and add a line
with open("example.txt", "a") as file:
    file.write("\nThis line was appended.")
