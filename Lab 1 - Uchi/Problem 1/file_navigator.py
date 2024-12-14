# This program allows the user to navigate through the lines of a text file.

def file_navigator():
    """Navigate through lines in a text file based on user input."""
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines into a list

        if not lines:
            print("The file is empty.")
            return

        while True:
            print(f"The file has {len(lines)} lines.")
            line_number = int(input("Enter a line number (0 to quit): "))
            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= len(lines):
                print(lines[line_number - 1].strip())  # Print the specified line
            else:
                print("Invalid line number. Try again.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")

if __name__ == "__main__":
    file_navigator()
