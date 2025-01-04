""" 
 PROBLEM 02:
 Write a program that allows the user to navigate the lines of text in a file. The program should prompt the user for a filename and input the lines of text into a list. 
 The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file.
 If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.
""" 

def view_file_lines():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
        total_lines = len(lines)
        print(f"File '{filename}' has {total_lines} lines.")
        while True:
            try:
                line_num = int(input("Enter line number (0 to exit): "))
                if line_num == 0:
                    print("Goodbye!")
                    break
                elif 1 <= line_num <= total_lines:
                    print(f"Line {line_num}: {lines[line_num - 1].strip()}")
                else:
                    print(f"Choose a number between 1 and {total_lines}, or 0 to exit.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    except FileNotFoundError:
        print("File not found. Try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    view_file_lines()

