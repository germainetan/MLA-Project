import os
import random
from shutil import copy2

# Set your source directory containing images
source_directory = "final_82"

# Set your destination directories for train and test datasets
train_directory = "train_images"
test_directory = "test_images"

# Create destination directories if they don't exist
os.makedirs(train_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# List subdirectories in the source directory
subdirectories = [d for d in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, d))]

# Initialize counters for each dataset
train_count = 0
test_count = 0

# Loop through subdirectories and copy images to the respective datasets
for subdirectory in subdirectories:
    subdirectory_path = os.path.join(source_directory, subdirectory)
    subdirectory_images = [f for f in os.listdir(subdirectory_path) if f.endswith(".jpg") or f.endswith(".png")]

    # Shuffle the images in each subdirectory
    random.shuffle(subdirectory_images)

    # Calculate the sizes of each dataset for this subdirectory
    total_images = len(subdirectory_images)
    train_size = int(0.9 * total_images)
    test_size = total_images - train_size

    # Split the images for this subdirectory into train and test sets
    train_images = subdirectory_images[:train_size]
    test_images = subdirectory_images[train_size:]

    # Create corresponding subdirectories in train and test directories
    train_subdirectory_path = os.path.join(train_directory, subdirectory)
    test_subdirectory_path = os.path.join(test_directory, subdirectory)

    os.makedirs(train_subdirectory_path, exist_ok=True)
    os.makedirs(test_subdirectory_path, exist_ok=True)

    # Copy images to the train and test directories
    for image in train_images:
        src_path = os.path.join(subdirectory_path, image)
        dst_path = os.path.join(train_subdirectory_path, image)
        copy2(src_path, dst_path)

    for image in test_images:
        src_path = os.path.join(subdirectory_path, image)
        dst_path = os.path.join(test_subdirectory_path, image)
        copy2(src_path, dst_path)

print("Splitting completed. Train: 90%, Test: 10%")
