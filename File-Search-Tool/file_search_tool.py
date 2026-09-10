import os
from pathlib import Path
from datetime import datetime


# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    """Display the application header."""
    print(CYAN + "=" * 60 + RESET)
    print(CYAN + "             SMART FILE SEARCH TOOL" + RESET)
    print(CYAN + "=" * 60 + RESET)


def format_size(size):
    """Convert file size from bytes into a readable format."""

    if size < 1024:
        return f"{size} B"

    elif size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"

    elif size < 1024 ** 3:
        return f"{size / (1024 ** 2):.2f} MB"

    else:
        return f"{size / (1024 ** 3):.2f} GB"


def get_file_details(file_path):
    """Return useful information about a file."""

    try:
        file_size = file_path.stat().st_size
        modified_time = file_path.stat().st_mtime

        modified_date = datetime.fromtimestamp(
            modified_time
        ).strftime("%Y-%m-%d %H:%M:%S")

        return file_size, modified_date

    except (PermissionError, OSError):
        return 0, "Unknown"


def display_results(results):
    """Display search results."""

    print()

    if not results:
        print(RED + "No files found." + RESET)
        return

    print(GREEN + "-" * 60 + RESET)
    print(GREEN + f"Files Found: {len(results)}" + RESET)
    print(GREEN + "-" * 60 + RESET)

    for number, file_path in enumerate(results, start=1):

        size, modified = get_file_details(file_path)

        print()
        print(YELLOW + f"{number}. {file_path.name}" + RESET)
        print(WHITE + f"   Location : {file_path}" + RESET)
        print(WHITE + f"   Size     : {format_size(size)}" + RESET)
        print(WHITE + f"   Modified : {modified}" + RESET)

    print()
    print(GREEN + "-" * 60 + RESET)
    print(GREEN + f"Total files found: {len(results)}" + RESET)
    print(GREEN + "-" * 60 + RESET)


def get_folder():
    """Ask the user for a folder path and validate it."""

    folder = input(
        YELLOW + "\nEnter folder path: " + RESET
    ).strip()

    folder_path = Path(folder)

    if not folder_path.exists():
        print(RED + "Error: Folder does not exist." + RESET)
        return None

    if not folder_path.is_dir():
        print(RED + "Error: The path is not a folder." + RESET)
        return None

    return folder_path


def search_by_filename(folder):
    """Search files using a filename keyword."""

    keyword = input(
        YELLOW + "\nEnter filename keyword: " + RESET
    ).strip().lower()

    if not keyword:
        print(RED + "Keyword cannot be empty." + RESET)
        return

    results = []

    try:
        for file_path in folder.rglob("*"):

            if file_path.is_file():
                if keyword in file_path.name.lower():
                    results.append(file_path)

    except PermissionError:
        print(RED + "Permission denied while searching." + RESET)

    display_results(results)


def get_extensions():
    """Get multiple file extensions from the user."""

    extension_input = input(
        YELLOW
        + "\nEnter extensions separated by commas "
        + "(example: .py,.txt,.pdf): "
        + RESET
    )

    extensions = []

    for extension in extension_input.split(","):

        extension = extension.strip().lower()

        if extension:
            if not extension.startswith("."):
                extension = "." + extension

            extensions.append(extension)

    return extensions


def search_by_extension(folder):
    """Search files using one or multiple extensions."""

    extensions = get_extensions()

    if not extensions:
        print(RED + "Please enter at least one extension." + RESET)
        return

    results = []

    try:
        for file_path in folder.rglob("*"):

            if file_path.is_file():

                if file_path.suffix.lower() in extensions:
                    results.append(file_path)

    except PermissionError:
        print(RED + "Permission denied while searching." + RESET)

    display_results(results)


def search_by_name_and_extension(folder):
    """Search files using both filename and extension."""

    keyword = input(
        YELLOW + "\nEnter filename keyword: " + RESET
    ).strip().lower()

    if not keyword:
        print(RED + "Keyword cannot be empty." + RESET)
        return

    extensions = get_extensions()

    if not extensions:
        print(RED + "Please enter at least one extension." + RESET)
        return

    results = []

    try:
        for file_path in folder.rglob("*"):

            if file_path.is_file():

                name_matches = keyword in file_path.name.lower()
                extension_matches = file_path.suffix.lower() in extensions

                if name_matches and extension_matches:
                    results.append(file_path)

    except PermissionError:
        print(RED + "Permission denied while searching." + RESET)

    display_results(results)


def search_by_size(folder):
    """Find files larger than a specified size."""

    try:
        minimum_size = float(
            input(
                YELLOW
                + "\nFind files larger than (MB): "
                + RESET
            )
        )

        minimum_bytes = minimum_size * 1024 * 1024

    except ValueError:
        print(RED + "Please enter a valid number." + RESET)
        return

    results = []

    try:
        for file_path in folder.rglob("*"):

            if file_path.is_file():

                try:
                    if file_path.stat().st_size > minimum_bytes:
                        results.append(file_path)

                except (PermissionError, OSError):
                    continue

    except PermissionError:
        print(RED + "Permission denied while searching." + RESET)

    display_results(results)


def show_all_files(folder):
    """Display all files inside the folder and subfolders."""

    results = []

    try:
        for file_path in folder.rglob("*"):

            if file_path.is_file():
                results.append(file_path)

    except PermissionError:
        print(RED + "Permission denied while searching." + RESET)

    display_results(results)


def show_menu():
    """Display the main menu."""

    print()
    print(BLUE + "1." + RESET + " Search by filename")
    print(BLUE + "2." + RESET + " Search by extension")
    print(BLUE + "3." + RESET + " Search by filename + extension")
    print(BLUE + "4." + RESET + " Find files larger than a size")
    print(BLUE + "5." + RESET + " Show all files")
    print(BLUE + "6." + RESET + " Change folder")
    print(BLUE + "7." + RESET + " Exit")


def main():
    """Main program."""

    clear_screen()
    print_header()

    folder = get_folder()

    if folder is None:
        input("\nPress Enter to exit...")
        return

    while True:

        clear_screen()
        print_header()

        print(
            GREEN
            + f"\nCurrent Folder: {folder}"
            + RESET
        )

        show_menu()

        choice = input(
            YELLOW + "\nEnter your choice: " + RESET
        ).strip()

        if choice == "1":
            search_by_filename(folder)

        elif choice == "2":
            search_by_extension(folder)

        elif choice == "3":
            search_by_name_and_extension(folder)

        elif choice == "4":
            search_by_size(folder)

        elif choice == "5":
            show_all_files(folder)

        elif choice == "6":
            new_folder = get_folder()

            if new_folder:
                folder = new_folder

        elif choice == "7":
            print(
                GREEN
                + "\nThank you for using Smart File Search Tool!"
                + RESET
            )
            break

        else:
            print(
                RED
                + "\nInvalid choice. Please select 1-7."
                + RESET
            )

        if choice != "7":
            input(
                CYAN
                + "\nPress Enter to continue..."
                + RESET
            )


if __name__ == "__main__":
    main()