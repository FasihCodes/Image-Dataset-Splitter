import os
import shutil
import random


def split_files(source_folder, train_ratio=0.8, val_ratio=0.2):
    # Ensure ratios sum to 1.0
    assert train_ratio + val_ratio == 1.0, "Ratios must sum to 1.0"

    # Get a list of all files in the source folder
    all_files = [os.path.join(source_folder, f) for f in os.listdir(source_folder) if
                 os.path.isfile(os.path.join(source_folder, f))]

    # Shuffle the files to ensure randomness
    random.shuffle(all_files)

    # Calculate the number of training and validation files
    train_count = int(len(all_files) * train_ratio)

    # Split the files
    train_files = all_files[:train_count]
    val_files = all_files[train_count:]

    return {'train': train_files, 'val': val_files}


# Get the current working directory
current_directory = os.getcwd()

# Define the source folder containing the images
folder_path = os.path.join(current_directory, 'others')

# Define the destination directories for train and valid
train_dir = os.path.join(current_directory, 'train-others')
valid_dir = os.path.join(current_directory, 'valid-others')

# Ensure the destination directories exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)

# Perform the custom split
split_result = split_files(folder_path, train_ratio=0.8, val_ratio=0.2)


# Function to move files to the corresponding directories
def move_files(file_list, destination_folder):
    for file_path in file_list:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination_path)


# Move the split files to the corresponding directories
move_files(split_result['train'], train_dir)
move_files(split_result['val'], valid_dir)

print("Files have been successfully split and moved.")
