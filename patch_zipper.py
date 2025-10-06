import zipfile
from pathlib import Path

def zip_patch_files(root_dir: str) -> None:
    """
    Recursively traverse all subdirectories of root_dir.
    For any subdirectory containing .bps, .ups, or .xdelta files, create a zip named after
    the subdirectory and place it in the parent directory.
    Files in the root directory itself are ignored.
    Any zip larger than limitMB is deleted, and an error message is shown.
    Skips hidden directories (any part of the path starting with ".").
    Patch files are added newest-first (by modification time).
    """
    limitMB = 100
    root_path = Path(root_dir)

    for subdir_path in root_path.rglob('*'):
        if subdir_path.is_dir():

            if any(part.startswith('.') for part in subdir_path.parts):
                continue

            patch_files = [
                f for f in subdir_path.iterdir()
                if f.is_file() and not f.name.startswith('.') and f.suffix.lower() in (".bps", ".ups", ".xdelta")
            ]
            
            if not patch_files:
                continue

            patch_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
            zip_name = f"{subdir_path.name}.zip"
            zip_path = subdir_path.parent / zip_name

            with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                for file_path in patch_files:
                    zipf.write(file_path, arcname=file_path.name)

            zip_size = zip_path.stat().st_size
            size_mb = zip_size / (1024 * 1024)

            if size_mb > limitMB:
                print(f"ERROR: {zip_path} exceeds {limitMB} MB ({size_mb:.2f} MB). Removing it.")
                zip_path.unlink(missing_ok=True)
            else:
                print(f"Created zip: {zip_path} with {len(patch_files)} file(s), size: {size_mb:.2f} MB.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <root_directory>")
        sys.exit(1)

    root_directory = Path(sys.argv[1])
    if not root_directory.is_dir():
        print("Error: Provided path is not a directory.")
        sys.exit(1)

    zip_patch_files(root_directory)
