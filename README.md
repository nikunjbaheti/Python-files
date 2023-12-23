# File Name Cleaner

This Python script removes annoying website names from music files and handles file names starting with numbers to avoid search problems.

## Author

- **Kshitiz Joshi**
- **Email:** joshikshitij_13@yahoo.in

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/file-name-cleaner.git
    cd file-name-cleaner
    ```

2. **Run the Script:**
    ```bash
    python file_name_cleaner.py
    ```

3. **Enter the Path to the Folder:**
    ```bash
    Enter the path to the folder: /path/to/your/folder
    ```

4. **Review Output:**
    - The script will display the old and new file names for each renamed file.
    - If an error occurs during the renaming process, an error message will be displayed.

## File Formats Supported

- .mp3
- .mp4
- .wma
- .wav
- .ogg
- .mid
- .ra
- .ram
- .rm

## Regular Expressions Used

1. `regex_web_name`: Matches annoying website names surrounded by parentheses, brackets, or curly braces.
2. `regex_num_start`: Matches numbers at the beginning of the file name, possibly followed by a dot or hyphen.

## Improvements Made

- Fixed the issue with `exit` by calling it as a function (`exit()`).
- Replaced `WindowsError` with `OSError` for better cross-platform compatibility.
- Used `os.path.join` to create file paths.
- Used `os.listdir` and `os.path.isfile` for listing files and checking if a path is a file.
- Changed the function to return early if the folder is not found.

Feel free to use and modify the script according to your needs!
