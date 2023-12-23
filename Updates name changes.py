import os
import re

def remove_website_names_and_numbers(folder_path):
    file_formats = ['.mp3', '.mp4', '.wma', '.wav', '.ogg', '.mid', '.ra', '.ram', '.rm']
    regex_web_name = r'\s*\-*\s*[\(\[\{]\S*\.\S*[\)\]\}]\s*'
    regex_num_start = r'^[0-9]+\s*[\-\.]?\s*'

    try:
        original_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except FileNotFoundError:
        print("Incorrect location")
        return

    for file_name in original_files:
        if any(file_name.lower().endswith(ext) for ext in file_formats):
            match_web = True
            match_num = True

            while match_web or match_num:
                match_web = re.search(regex_web_name, file_name)
                match_num = re.search(regex_num_start, file_name)

                if match_web and match_num:
                    new_name = file_name.replace(match_web.group(), "").replace(match_num.group(), "")
                elif match_num:
                    new_name = file_name.replace(match_num.group(), "")
                elif match_web:
                    new_name = file_name.replace(match_web.group(), "")
                else:
                    continue

                new_file_path = os.path.join(folder_path, new_name)

                try:
                    os.rename(os.path.join(folder_path, file_name), new_file_path)
                except OSError as e:
                    print(f"Error renaming file: {file_name} to {new_name}. Error: {e}")
                    match_web = False
                    match_num = False
                    continue

                print("Old Name:", file_name)
                print("New Name:", new_name)
                print("--------------------------------------")
                file_name = new_name

# Example usage:
folder_path = input("Enter the path to the folder: ")
remove_website_names_and_numbers(folder_path)
