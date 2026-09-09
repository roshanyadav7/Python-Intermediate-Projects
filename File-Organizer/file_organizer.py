import os
import shutil
from pathlib import Path
from datetime import datetime


# File categories and their extensions
FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".ppt", ".pptx", ".odt"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".csv"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov", ".wmv", ".flv"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg", ".m4a"
    ],

    "Archives": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz"
    ],

    "Code": [
        ".py", ".java", ".c", ".cpp",
        ".html", ".css", ".js",
        ".php", ".sql"
    ]
}


def get_category(file_extension):
    """
    Find the category of a file based on its extension.
    """

    file_extension = file_extension.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if file_extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination_folder, filename):
    """
    Create a unique filename if a file with the same
    name already exists.
    """

    destination = destination_folder / filename

    if not destination.exists():
        return destination

    name = destination.stem
    extension = destination.suffix

    counter = 1

    while True:
        new_filename = f"{name}_{counter}{extension}"
        new_destination = destination_folder / new_filename

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path, preview=False):
    """
    Organize files inside the selected folder.
    """

    folder = Path(folder_path)

    if not folder.exists():
        print("\n❌ Error: The folder does not exist.")
        return

    if not folder.is_dir():
        print("\n❌ Error: The provided path is not a folder.")
        return

    moved_files = 0
    skipped_files = 0
    category_count = {}

    print("\n" + "=" * 60)

    if preview:
        print("FILE ORGANIZER - PREVIEW MODE")
    else:
        print("FILE ORGANIZER")

    print("=" * 60)

    # Get only files from the selected folder
    files = [
        item for item in folder.iterdir()
        if item.is_file()
    ]

    if not files:
        print("\n📂 No files found in this folder.")
        return

    print(f"\nFound {len(files)} file(s).\n")

    for file in files:

        # Do not move the Python program itself
        if file.name == Path(__file__).name:
            skipped_files += 1
            continue

        extension = file.suffix
        category = get_category(extension)

        destination_folder = folder / category

        destination_file = get_unique_destination(
            destination_folder,
            file.name
        )

        if preview:

            print(
                f"📄 {file.name}  →  {category}/"
            )

            moved_files += 1

        else:

            try:
                # Create category folder if it doesn't exist
                destination_folder.mkdir(
                    parents=True,
                    exist_ok=True
                )

                # Move the file
                shutil.move(
                    str(file),
                    str(destination_file)
                )

                print(
                    f"✅ {file.name}  →  {category}/"
                )

                moved_files += 1

                # Count files in each category
                category_count[category] = (
                    category_count.get(category, 0) + 1
                )

            except PermissionError:
                print(
                    f"⚠️ Permission denied: {file.name}"
                )
                skipped_files += 1

            except OSError as error:
                print(
                    f"⚠️ Could not move {file.name}: {error}"
                )
                skipped_files += 1

    # Summary
    print("\n" + "=" * 60)
    print("ORGANIZATION SUMMARY")
    print("=" * 60)

    if preview:
        print(f"Files that would be organized: {moved_files}")
    else:
        print(f"Files organized: {moved_files}")
        print(f"Files skipped: {skipped_files}")

        if category_count:
            print("\nFiles by category:")

            for category, count in category_count.items():
                print(f"  {category}: {count}")

    print("=" * 60)


def create_log(folder_path):
    """
    Create a simple log file containing the time
    at which the organizer was executed.
    """

    folder = Path(folder_path)

    log_file = folder / "organization_log.txt"

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    try:

        with open(log_file, "a", encoding="utf-8") as file:

            file.write(
                f"File Organizer executed: {current_time}\n"
            )

        print(f"\n📝 Log saved to: {log_file.name}")

    except OSError as error:

        print(f"\n⚠️ Could not create log: {error}")


def main():

    print("\n" + "=" * 60)
    print("          SMART FILE ORGANIZER")
    print("=" * 60)

    print("\nThis program organizes files based on their type.")

    folder_path = input(
        "\nEnter the folder path to organize: "
    ).strip()

    if not folder_path:
        print("\n❌ Folder path cannot be empty.")
        return

    # Remove quotes if the user copied a quoted Windows path
    folder_path = folder_path.strip('"')

    print("\nChoose an option:")
    print("1. Preview organization")
    print("2. Organize files")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":

        organize_files(
            folder_path,
            preview=True
        )

    elif choice == "2":

        organize_files(
            folder_path,
            preview=False
        )

        create_log(folder_path)

    elif choice == "3":

        print("\n👋 Program closed.")

    else:

        print("\n❌ Invalid choice.")


if __name__ == "__main__":
    main()