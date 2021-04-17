from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from datetime import datetime
from time import gmtime, strftime


class Cleanup(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != "REPLACE_WITH_FOLDER_NAME":
                new_name = filename
                extension = "noname"
                try:
                    extension = str(
                        os.path.splitext(folder_to_track + "/" + filename)[1]
                    )
                except Exception:
                    extension = "noname"

                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = extensions_folders[extension]

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]):
                    if folder_name == year:
                        folder_destination_path = (
                            extensions_folders[extension] + "/" + year
                        )
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = (
                                    extensions_folders[extension]
                                    + "/"
                                    + year
                                    + "/"
                                    + month
                                )
                                month_exists = True
                if not year_exists:
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    folder_destination_path = extensions_folders[extension] + "/" + year
                if not month_exists:
                    os.mkdir(folder_destination_path + "/" + month)
                    folder_destination_path = folder_destination_path + "/" + month

                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                while file_exists:
                    i += 1
                    new_name = (
                        os.path.splitext(folder_to_track + "/" + filename)[0]
                        + str(i)
                        + os.path.splitext(folder_to_track + "/" + filename)[1]
                    )
                    new_name = new_name.split("/")[2]
                    print(new_name)
                    file_exists = os.path.isfile(
                        folder_destination_path + "/" + new_name
                    )
                src = folder_to_track + "/" + filename

                new_name = folder_destination_path + "/" + new_name
                os.rename(src, new_name)


folder_to_track = "path_for_folder_to_track"
folder_destination = "path_for_folder_destination"

extensions_folders = {
    # No name
    "noname": os.path.join(folder_destination, "Other", "Uncategorized"),
    # Audio
    ".aif": os.path.join(folder_destination, "Media", "Audio"),
    ".cda": os.path.join(folder_destination, "Media", "Audio"),
    ".mid": os.path.join(folder_destination, "Media", "Audio"),
    ".midi": os.path.join(folder_destination, "Media", "Audio"),
    ".mp3": os.path.join(folder_destination, "Media", "Audio"),
    ".mpa": os.path.join(folder_destination, "Media", "Audio"),
    ".ogg": os.path.join(folder_destination, "Media", "Audio"),
    ".wav": os.path.join(folder_destination, "Media", "Audio"),
    ".wma": os.path.join(folder_destination, "Media", "Audio"),
    ".wpl": os.path.join(folder_destination, "Media", "Audio"),
    ".m3u": os.path.join(folder_destination, "Media", "Audio"),
    # Text
    ".txt": os.path.join(folder_destination, "Text", "TextFiles"),
    ".doc": os.path.join(folder_destination, "Text", "Microsoft", "Word"),
    ".docx": os.path.join(folder_destination, "Text", "Microsoft", "Word"),
    ".odt ": os.path.join(folder_destination, "Text", "TextFiles"),
    ".pdf": os.path.join(folder_destination, "Text", "PDF"),
    ".rtf": os.path.join(folder_destination, "Text", "TextFiles"),
    ".tex": os.path.join(folder_destination, "Text", "TextFiles"),
    ".wks ": os.path.join(folder_destination, "Text", "TextFiles"),
    ".wps": os.path.join(folder_destination, "Text", "TextFiles"),
    ".wpd": os.path.join(folder_destination, "Text", "TextFiles"),
    # Video
    ".3g2": os.path.join(folder_destination, "Media", "Video"),
    ".3gp": os.path.join(folder_destination, "Media", "Video"),
    ".avi": os.path.join(folder_destination, "Media", "Video"),
    ".flv": os.path.join(folder_destination, "Media", "Video"),
    ".h264": os.path.join(folder_destination, "Media", "Video"),
    ".m4v": os.path.join(folder_destination, "Media", "Video"),
    ".mkv": os.path.join(folder_destination, "Media", "Video"),
    ".mov": os.path.join(folder_destination, "Media", "Video"),
    ".mp4": os.path.join(folder_destination, "Media", "Video"),
    ".mpg": os.path.join(folder_destination, "Media", "Video"),
    ".mpeg": os.path.join(folder_destination, "Media", "Video"),
    ".rm": os.path.join(folder_destination, "Media", "Video"),
    ".swf": os.path.join(folder_destination, "Media", "Video"),
    ".vob": os.path.join(folder_destination, "Media", "Video"),
    ".wmv": os.path.join(folder_destination, "Media", "Video"),
    # Images
    ".ai": os.path.join(folder_destination, "Media", "Images"),
    ".bmp": os.path.join(folder_destination, "Media", "Images"),
    ".gif": os.path.join(folder_destination, "Media", "Images"),
    ".ico": os.path.join(folder_destination, "Media", "Images"),
    ".jpg": os.path.join(folder_destination, "Media", "Images"),
    ".jpeg": os.path.join(folder_destination, "Media", "Images"),
    ".png": os.path.join(folder_destination, "Media", "Images"),
    ".ps": os.path.join(folder_destination, "Media", "Images"),
    ".psd": os.path.join(folder_destination, "Media", "Images"),
    ".svg": os.path.join(folder_destination, "Media", "Images"),
    ".tif": os.path.join(folder_destination, "Media", "Images"),
    ".tiff": os.path.join(folder_destination, "Media", "Images"),
    ".CR2": os.path.join(folder_destination, "Media", "Images"),
    # Internet
    ".asp": os.path.join(folder_destination, "Other", "Internet"),
    ".aspx": os.path.join(folder_destination, "Other", "Internet"),
    ".cer": os.path.join(folder_destination, "Other", "Internet"),
    ".cfm": os.path.join(folder_destination, "Other", "Internet"),
    ".cgi": os.path.join(folder_destination, "Other", "Internet"),
    ".pl": os.path.join(folder_destination, "Other", "Internet"),
    ".css": os.path.join(folder_destination, "Other", "Internet"),
    ".htm": os.path.join(folder_destination, "Other", "Internet"),
    ".js": os.path.join(folder_destination, "Other", "Internet"),
    ".jsp": os.path.join(folder_destination, "Other", "Internet"),
    ".part": os.path.join(folder_destination, "Other", "Internet"),
    ".php": os.path.join(folder_destination, "Other", "Internet"),
    ".rss": os.path.join(folder_destination, "Other", "Internet"),
    ".xhtml": os.path.join(folder_destination, "Other", "Internet"),
    # Compressed
    ".7z": os.path.join(folder_destination, "Other", "Compressed"),
    ".arj": os.path.join(folder_destination, "Other", "Compressed"),
    ".deb": os.path.join(folder_destination, "Other", "Compressed"),
    ".pkg": os.path.join(folder_destination, "Other", "Compressed"),
    ".rar": os.path.join(folder_destination, "Other", "Compressed"),
    ".rpm": os.path.join(folder_destination, "Other", "Compressed"),
    ".tar.gz": os.path.join(folder_destination, "Other", "Compressed"),
    ".z": os.path.join(folder_destination, "Other", "Compressed"),
    ".zip": os.path.join(folder_destination, "Other", "Compressed"),
    # Disc
    ".bin": os.path.join(folder_destination, "Other", "Disc"),
    ".dmg": os.path.join(folder_destination, "Other", "Disc"),
    ".iso": os.path.join(folder_destination, "Other", "Disc"),
    ".toast": os.path.join(folder_destination, "Other", "Disc"),
    ".vcd": os.path.join(folder_destination, "Other", "Disc"),
    # Data
    ".csv": os.path.join(folder_destination, "Programming", "Database"),
    ".dat": os.path.join(folder_destination, "Programming", "Database"),
    ".db": os.path.join(folder_destination, "Programming", "Database"),
    ".dbf": os.path.join(folder_destination, "Programming", "Database"),
    ".log": os.path.join(folder_destination, "Programming", "Database"),
    ".mdb": os.path.join(folder_destination, "Programming", "Database"),
    ".sav": os.path.join(folder_destination, "Programming", "Database"),
    ".sql": os.path.join(folder_destination, "Programming", "Database"),
    ".tar": os.path.join(folder_destination, "Programming", "Database"),
    ".xml": os.path.join(folder_destination, "Programming", "Database"),
    ".json": os.path.join(folder_destination, "Programming", "Database"),
    # Executables
    ".apk": os.path.join(folder_destination, "Other", "Executables"),
    ".bat": os.path.join(folder_destination, "Other", "Executables"),
    ".com": os.path.join(folder_destination, "Other", "Executables"),
    ".exe": os.path.join(folder_destination, "Other", "Executables"),
    ".gadget": os.path.join(folder_destination, "Other", "Executables"),
    ".jar": os.path.join(folder_destination, "Other", "Executables"),
    ".wsf": os.path.join(folder_destination, "Other", "Executables"),
    # Fonts
    ".fnt": os.path.join(folder_destination, "Other", "Fonts"),
    ".fon": os.path.join(folder_destination, "Other", "Fonts"),
    ".otf": os.path.join(folder_destination, "Other", "Fonts"),
    ".ttf": os.path.join(folder_destination, "Other", "Fonts"),
    # Presentations
    ".key": os.path.join(folder_destination, "Text", "Presentations"),
    ".odp": os.path.join(folder_destination, "Text", "Presentations"),
    ".pps": os.path.join(folder_destination, "Text", "Presentations"),
    ".ppt": os.path.join(folder_destination, "Text", "Presentations"),
    ".pptx": os.path.join(folder_destination, "Text", "Presentations"),
    # Programming
    ".c": os.path.join(folder_destination, "Programming", "C&C++"),
    ".class": os.path.join(folder_destination, "Programming", "Java"),
    ".dart": os.path.join(folder_destination, "Programming", "Dart"),
    ".py": os.path.join(folder_destination, "Programming", "Python"),
    ".go": os.path.join(folder_destination, "Programming", "Go"),
    ".sh": os.path.join(folder_destination, "Programming", "Shell"),
    ".swift": os.path.join(folder_destination, "Programming", "Swift"),
    ".html": os.path.join(folder_destination, "Programming", "C&C++"),
    ".h": os.path.join(folder_destination, "Programming", "C&C++"),
    # Spreadsheets
    ".ods": os.path.join(folder_destination, "Text", "Microsoft", "Excel"),
    ".xlr": os.path.join(folder_destination, "Text", "Microsoft", "Excel"),
    ".xls": os.path.join(folder_destination, "Text", "Microsoft", "Excel"),
    ".xlsx": os.path.join(folder_destination, "Text", "Microsoft", "Excel"),
    # System
    ".bak": os.path.join(folder_destination, "Text", "Other", "System"),
    ".cab": os.path.join(folder_destination, "Text", "Other", "System"),
    ".cfg": os.path.join(folder_destination, "Text", "Other", "System"),
    ".cpl": os.path.join(folder_destination, "Text", "Other", "System"),
    ".cur": os.path.join(folder_destination, "Text", "Other", "System"),
    ".dll": os.path.join(folder_destination, "Text", "Other", "System"),
    ".dmp": os.path.join(folder_destination, "Text", "Other", "System"),
    ".drv": os.path.join(folder_destination, "Text", "Other", "System"),
    ".icns": os.path.join(folder_destination, "Text", "Other", "System"),
    ".ini": os.path.join(folder_destination, "Text", "Other", "System"),
    ".lnk": os.path.join(folder_destination, "Text", "Other", "System"),
    ".msi": os.path.join(folder_destination, "Text", "Other", "System"),
    ".sys": os.path.join(folder_destination, "Text", "Other", "System"),
    ".tmp": os.path.join(folder_destination, "Text", "Other", "System"),
}

event_handler = Cleanup()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    observer.stop()


observer.join()
