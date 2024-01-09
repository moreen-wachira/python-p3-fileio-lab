# lib/file_io.py

def write_file(file_name, file_content):
    # Combine file name with extension
    file_name_with_extension = file_name + ".txt"
    
    # Open file for writing
    with open(file_name_with_extension, 'w') as file:
        # Write content to the file
        file.write(file_content)

def append_to_file(file_name, append_content):
    # Combine file name with extension
    file_name_with_extension = file_name + ".txt"
    
    # Open file for appending
    with open(file_name_with_extension, 'a') as file:
        # Append content to the file
        file.write("\n" + append_content)

def read_file(file_name):
    # Combine file name with extension
    file_name_with_extension = file_name + ".txt"
    
    # Open file for reading
    with open(file_name_with_extension, 'r') as file:
        # Read and return the content of the file
        return file.read()
