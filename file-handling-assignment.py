



try:
    # Creating a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Writing three lines of text to the file
        file.write("This is line 1.\n")
        file.write("Line 2 has a mix of strings and numbers: 12345.\n")
        file.write("Another line with text and numbers: 3.14\n")

    # Reading and displaying the contents of "my_file.txt"
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # Opening "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text to the existing content
        file.write("This is an appended line.\n")
        file.write("Appending another line with numbers: 67890.\n")
        file.write("Final appended line with more text.\n")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", e)

finally:
    print("Execution completed.")
