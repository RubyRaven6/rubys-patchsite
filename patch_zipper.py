import zipfile
from pathlib import Path

def zip_patch_files(root_dir: str) -> None:
    """
    Recursively traverse all subdirectories of root_dir.
    For any subdirectory containing .bps or .ups files, create a zip named after
    the subdirectory and place it in the parent directory.
    Files in the root directory itself are ignored.
    """
    root_path = Path(root_dir)

    for subdir_path in root_path.rglob('*'):
        if subdir_path.is_dir():
            patch_files = [f for f in subdir_path.iterdir() if f.is_file() and f.suffix.lower() in (".bps", ".ups", ".xdelta")]
            
            if not patch_files:
                continue

            zip_name = f"{subdir_path.name}.zip"
            zip_path = subdir_path.parent / zip_name

            with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                for file_path in patch_files:
                    zipf.write(file_path, arcname=file_path.name)

            print(f"Created zip: {zip_path} with {len(patch_files)} file(s).")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    root_path = Path(root_directory)
    if not root_path.is_dir():
        print("Error: Provided path is not a directory.")
        sys.exit(1)

    zip_patch_files(root_directory)
