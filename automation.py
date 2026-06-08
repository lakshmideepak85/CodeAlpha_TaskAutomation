import os
import shutil

print("JPG File Automation Tool")

source_folder = input("Enter Source Folder Path: ")
destination_folder = input("Enter Destination Folder Path: ")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

count = 0

for file in os.listdir(source_folder):

    if file.endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        count += 1
        print(f"Moved: {file}")

print("\nTask Completed Successfully!")
print(f"Total JPG Files Moved: {count}")