# navigator.py: A program to navigate through lines of a text file

def display_file_line_count(filename):
    """Displays the total number of lines in the file."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
        return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def navigate_lines(lines):
    """Allows the user to navigate through the lines of the file."""
    print(f"The file has {len(lines)} lines.")
    
    while True:
        line_number = input("Enter a line number (1 to exit, 0 to quit): ")
        
        if line_number == "0":
            print("Exiting the program.")
            break
        elif line_number == "1":
            print("Exiting the program.")
            break
        elif line_number.isdigit() and 1 <= int(line_number) <= len(lines):
            # Display the selected line
            print(lines[int(line_number) - 1].strip())
        else:
            print("Invalid line number. Please try again.")

def file_navigator():
    """Main function to handle file navigation."""
    filename = input("Enter the filename: ")
    
    # Read file and get lines
    lines = display_file_line_count(filename)
    if lines:
        navigate_lines(lines)

if __name__ == "__main__":
    file_navigator()
