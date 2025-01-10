"""
Simple program to navigate lines of text in a file.
"""
def main():
    filename = input("Enter the file name: ")
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()

        print(f"This file has {len(lines)} lines.")

        while True:
            line_num = input("Enter a line number (0 to quit): ")
            if not line_num.isdigit():
                print("Please enter a valid number.")
                continue

            line_num = int(line_num)

            if line_num == 0:
                print("Goodbye!")
                break
            elif 1 <= line_num <= len(lines):
                print(lines[line_num - 1].strip())
            else:
                print("Line number out of range.")
    except FileNotFoundError:
        print("File not found. Please check the file name.")

if __name__ == "__main__":
    main()
