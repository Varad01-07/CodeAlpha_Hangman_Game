import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"📁 Created destination folder: {destination_folder}")
    
    # Track moved files
    moved_files = 0
    
    # Iterate over files in the source folder
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            
            shutil.move(source_path, destination_path)
            moved_files += 1
            print(f"✅ Moved: {file_name}")
    
    if moved_files == 0:
        print("⚠ No .jpg files found in the source folder.")
    else:
        print(f"🎉 Successfully moved {moved_files} .jpg files to '{destination_folder}'.")

if __name__ == "__main__":
    src = input("Enter the source folder path: ").strip()
    dest = input("Enter the destination folder path: ").strip()
    move_jpg_files(src, dest)
