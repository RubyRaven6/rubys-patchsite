import shutil
import os
import sys

def copy_template(destination_name, overwrite=False):
    if destination_name == '.':
        print(f"Cannot use '{destination_name}' as destination.")
        return

    source = "./hacks/template"
    destination = f"./hacks/{destination_name}"
    patches_dir = os.path.join(destination, "patches")

    if not os.path.exists(source):
        print(f"Source folder '{source}' does not exist.")
        return

    if os.path.exists(destination):
        if overwrite:
            shutil.rmtree(destination)
            print(f"Removing folder '{destination}' for overwrite.")
        else:
            print(f"Destination folder '{destination}' already exists. Use overwrite=True to replace it.")
            return

    try:
        shutil.copytree(source, destination)
        os.makedirs(patches_dir, exist_ok=True)
        print(f"ROM Patching Page created successfully at '{destination}'")

    except Exception as e:
        print(f"Error copying folder: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python copy_folder.py <destination_folder_name> [overwrite]")
    else:
        dest_name = sys.argv[1]
        overwrite_flag = False
        if len(sys.argv) >= 3:
            overwrite_flag = sys.argv[2].lower() in ["true", "1", "yes"]
        copy_template(dest_name, overwrite_flag)
