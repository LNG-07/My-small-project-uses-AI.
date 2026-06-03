import os
import shutil

# Target directory path to be cleaned up
TARGET_DIR = r"Please paste the links you want to sort here."

# File classification dictionary
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Installers": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z"],
}

def clean_folder(target_directory):
    # Check if the target directory exists
    if not os.path.exists(target_directory):
        print("Directory does not exist! Please check the file path again.")
        return

    # Loop through each item in the directory
    for item in os.listdir(target_directory):
        item_path = os.path.join(target_directory, item)

        # Skip if it is a directory (we only process files)
        if os.path.isdir(item_path):
            continue

        # Get the file extension and convert it to lowercase
        _, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower()

        # Variable to check if the file has been categorized
        moved = False

        # Find the matching folder for the file type
        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                # Create the path for the new folder
                destination_folder = os.path.join(target_directory, folder_name)

                # Automatically create the folder if it does not exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # Move the file into the destination folder
                shutil.move(item_path, destination_folder)
                print(f"Moved: {item} -> Folder [{folder_name}]")
                moved = True
                break

        # If the file extension is not in the FILE_TYPES dictionary
        if not moved:
            other_folder = os.path.join(target_directory, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(item_path, other_folder)
            print(f"Moved: {item} -> Folder [Others]")

    print("\n Congratulations! Your folder has been successfully organized!")


if __name__ == "__main__":
    clean_folder(TARGET_DIR)
