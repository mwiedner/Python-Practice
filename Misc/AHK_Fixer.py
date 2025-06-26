import os

# === CONFIGURATION ===
folder = r"C:\Users\wiedn\OneDrive\Documents\GitHub\ahk"  # Folder to search
find_str = r"menu, tray, icon, % script_icon()"         # String to find
replace_str = "#Include ..\\.Functional\\script_icon.ahk\nTraySetIcon(script_icon())"  # String to replace with
ignore_files = {"Overlord.ahk", "Launcher.ahk"}  # Set of filenames to ignore (case-insensitive)
# =====================

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.lower().endswith('.ahk') and file.lower() not in {f.lower() for f in ignore_files}:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = content.replace(find_str, replace_str)
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file_path}")