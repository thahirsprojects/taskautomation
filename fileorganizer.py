import os
import shutil

def organize_downloads():
    """
    Organizes files in the user's Downloads directory into sub folders based on file type. 
    
    """
    try:
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        
        if not os.path.exists(downloads_dir):
            print("Downloads directory does not exist.")
            return

        file_types = {
            # Add the folder and file types to organize
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
            'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
            'Audio': ['.mp3', '.wav', '.aac'],
            'Archives': ['.zip', '.rar', '.tar', '.gz'],
            'data' : ['.csv','.xls','.xlsx','.db','.sql'],
            'Notebook' : ['.ipynb'],
            'Application' : ['.exe']
        }

        # Loop through all files in the Downloads directory
        for filename in os.listdir(downloads_dir):
            file_path = os.path.join(downloads_dir, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            # Identify the file type
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    # Create the folder if it doesn't exist
                    folder_path = os.path.join(downloads_dir, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    
                    # Move the file
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved: {filename} -> {folder}/")
                    moved = True
                    break
            
            # Handle files with unrecognized extensions
            if not moved:
                other_folder = os.path.join(downloads_dir, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved: {filename} -> Others/")

        print("\nOrganization of Downloads complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    organize_downloads()
