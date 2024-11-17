import os

def duplicate_file(file_path, num_copies=1):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    file_name, file_extension = os.path.splitext(file_path)
    for i in range(1, num_copies + 1):
        new_file = f"{file_name}_copy{i}{file_extension}"
        with open(file_path, 'rb') as original:
            with open(new_file, 'wb') as duplicate:
                duplicate.write(original.read())
        print(f"Duplicated: {new_file}")

file_path = input("Enter the path of the file to duplicate: ")
num_copies = int(input("Enter the number of copies to create: "))
duplicate_file(file_path, num_copies)
