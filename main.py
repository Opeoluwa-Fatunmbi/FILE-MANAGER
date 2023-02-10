import os

# Specify the directory where the files are located
directory = "/path/to/directory"

# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Get the file path
    file_path = os.path.join(directory, filename)
    # Split the file name and extension
    name, extension = os.path.splitext(filename)
    # Rename the file by adding a prefix to the name
    new_filename = "prefix_" + name + extension
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)
