#file_navigator.py
def navigate_file():
    #Filename prompt
    file_name = input("Input the file's name: ").strip()
    try:
        with open(file_name, 'r+', encoding='utf-8') as f:  #Reading and editing
            content_lines = f.readlines()  #Lines to list

        while True:
            print(f"\nThe document comprises {len(content_lines)} total lines.")
            user_input = input("Provide a line number to view or edit (use 0 to exit): ").strip()

            if user_input.isdigit():
                line_index = int(user_input)
                if line_index == 0:
                    print("Program terminated successfully.")
                    break
                elif 1 <= line_index <= len(content_lines):
                    print(f"Line {line_index}: {content_lines[line_index - 1].rstrip()}")
                    edit_input = input("Do you want to edit this line? (y/n): ").strip().lower()
                    if edit_input == 'y':
                        new_line = input(f"Enter new content for line {line_index}: ").strip()
                        content_lines[line_index - 1] = new_line + '\n'
                        f.seek(0)  #Back to the start of the file
                        f.writelines(content_lines)
                        print(f"Line {line_index} updated successfully.")
                else:
                    print("Error: Enter a number within the line range.")
            else:
                print("Error: Input must be a numeric value.")

    except FileNotFoundError:
        print("FileNotFoundError: Cannot locate the specified file.")
    except Exception as e:
        print(f"UnexpectedError: {e}")  #Error catching
      
if __name__ == "__main__":
    navigate_file()
