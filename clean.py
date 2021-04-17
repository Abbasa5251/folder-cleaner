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
        for filename in os.listdir(FOLDER_TO_TRACK):
            i = 1
            if filename != "REPLACE_WITH_FOLDER_NAME":
                new_name = filename
                extension = "noname"
                try:
                    extension = str(
                        os.path.splitext(FOLDER_TO_TRACK + "/" + filename)[1]
                    )
                except Exception:
                    extension = "noname"

                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                FOLDER_DESTINATION_PATH = extensions_folders[extension]

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]):
                    if folder_name == year:
                        FOLDER_DESTINATION_PATH = (
                            extensions_folders[extension] + "/" + year
                        )
                        year_exists = True
                        for folder_month in os.listdir(FOLDER_DESTINATION_PATH):
                            if month == folder_month:
                                FOLDER_DESTINATION_PATH = (
                                    extensions_folders[extension]
                                    + "/"
                                    + year
                                    + "/"
                                    + month
                                )
                                month_exists = True
                if not year_exists:
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    FOLDER_DESTINATION_PATH = extensions_folders[extension] + "/" + year
                if not month_exists:
                    os.mkdir(FOLDER_DESTINATION_PATH + "/" + month)
                    FOLDER_DESTINATION_PATH = FOLDER_DESTINATION_PATH + "/" + month

                file_exists = os.path.isfile(FOLDER_DESTINATION_PATH + "/" + new_name)
                while file_exists:
                    i += 1
                    new_name = (
                        os.path.splitext(FOLDER_TO_TRACK + "/" + filename)[0]
                        + str(i)
                        + os.path.splitext(FOLDER_TO_TRACK + "/" + filename)[1]
                    )
                    new_name = new_name.split("/")[2]
                    print(new_name)
                    file_exists = os.path.isfile(
                        FOLDER_DESTINATION_PATH + "/" + new_name
                    )
                src = FOLDER_TO_TRACK + "/" + filename

                new_name = FOLDER_DESTINATION_PATH + "/" + new_name
                os.rename(src, new_name)


FOLDER_TO_TRACK = "path_for_FOLDER_TO_TRACK"
FOLDER_DESTINATION = "path_for_FOLDER_DESTINATION"

extensions_folders = {
    # No name
    "noname": os.path.join(FOLDER_DESTINATION, "Other", "Uncategorized"),
    # Audio
    ".aif": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".cda": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".mid": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".midi": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".mp3": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".mpa": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".ogg": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".wav": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".wma": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".wpl": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    ".m3u": os.path.join(FOLDER_DESTINATION, "Media", "Audio"),
    # Text
    ".txt": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    ".doc": os.path.join(FOLDER_DESTINATION, "Text", "Microsoft", "Word"),
    ".docx": os.path.join(FOLDER_DESTINATION, "Text", "Microsoft", "Word"),
    ".odt ": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    ".pdf": os.path.join(FOLDER_DESTINATION, "Text", "PDF"),
    ".rtf": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    ".tex": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    ".wks ": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    ".wps": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    ".wpd": os.path.join(FOLDER_DESTINATION, "Text", "TextFiles"),
    # Video
    ".3g2": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".3gp": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".avi": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".flv": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".h264": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".m4v": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".mkv": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".mov": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".mp4": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".mpg": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".mpeg": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".rm": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".swf": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".vob": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    ".wmv": os.path.join(FOLDER_DESTINATION, "Media", "Video"),
    # Images
    ".ai": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".bmp": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".gif": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".ico": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".jpg": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".jpeg": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".png": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".ps": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".psd": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".svg": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".tif": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".tiff": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    ".CR2": os.path.join(FOLDER_DESTINATION, "Media", "Images"),
    # Internet
    ".asp": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".aspx": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".cer": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".cfm": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".cgi": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".pl": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".css": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".htm": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".js": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".jsp": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".part": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".php": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".rss": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    ".xhtml": os.path.join(FOLDER_DESTINATION, "Other", "Internet"),
    # Compressed
    ".7z": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".arj": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".deb": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".pkg": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".rar": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".rpm": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".tar.gz": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".z": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    ".zip": os.path.join(FOLDER_DESTINATION, "Other", "Compressed"),
    # Disc
    ".bin": os.path.join(FOLDER_DESTINATION, "Other", "Disc"),
    ".dmg": os.path.join(FOLDER_DESTINATION, "Other", "Disc"),
    ".iso": os.path.join(FOLDER_DESTINATION, "Other", "Disc"),
    ".toast": os.path.join(FOLDER_DESTINATION, "Other", "Disc"),
    ".vcd": os.path.join(FOLDER_DESTINATION, "Other", "Disc"),
    # Data
    ".csv": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".dat": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".db": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".dbf": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".log": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".mdb": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".sav": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".sql": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".tar": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".xml": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    ".json": os.path.join(FOLDER_DESTINATION, "Programming", "Database"),
    # Executables
    ".apk": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    ".bat": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    ".com": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    ".exe": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    ".gadget": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    ".jar": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    ".wsf": os.path.join(FOLDER_DESTINATION, "Other", "Executables"),
    # Fonts
    ".fnt": os.path.join(FOLDER_DESTINATION, "Other", "Fonts"),
    ".fon": os.path.join(FOLDER_DESTINATION, "Other", "Fonts"),
    ".otf": os.path.join(FOLDER_DESTINATION, "Other", "Fonts"),
    ".ttf": os.path.join(FOLDER_DESTINATION, "Other", "Fonts"),
    # Presentations
    ".key": os.path.join(FOLDER_DESTINATION, "Text", "Presentations"),
    ".odp": os.path.join(FOLDER_DESTINATION, "Text", "Presentations"),
    ".pps": os.path.join(FOLDER_DESTINATION, "Text", "Presentations"),
    ".ppt": os.path.join(FOLDER_DESTINATION, "Text", "Presentations"),
    ".pptx": os.path.join(FOLDER_DESTINATION, "Text", "Presentations"),
    # Programming
    ".c": os.path.join(FOLDER_DESTINATION, "Programming", "C&C++"),
    ".class": os.path.join(FOLDER_DESTINATION, "Programming", "Java"),
    ".dart": os.path.join(FOLDER_DESTINATION, "Programming", "Dart"),
    ".py": os.path.join(FOLDER_DESTINATION, "Programming", "Python"),
    ".go": os.path.join(FOLDER_DESTINATION, "Programming", "Go"),
    ".sh": os.path.join(FOLDER_DESTINATION, "Programming", "Shell"),
    ".swift": os.path.join(FOLDER_DESTINATION, "Programming", "Swift"),
    ".html": os.path.join(FOLDER_DESTINATION, "Programming", "C&C++"),
    ".h": os.path.join(FOLDER_DESTINATION, "Programming", "C&C++"),
    # Spreadsheets
    ".ods": os.path.join(FOLDER_DESTINATION, "Text", "Microsoft", "Excel"),
    ".xlr": os.path.join(FOLDER_DESTINATION, "Text", "Microsoft", "Excel"),
    ".xls": os.path.join(FOLDER_DESTINATION, "Text", "Microsoft", "Excel"),
    ".xlsx": os.path.join(FOLDER_DESTINATION, "Text", "Microsoft", "Excel"),
    # System
    ".bak": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".cab": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".cfg": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".cpl": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".cur": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".dll": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".dmp": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".drv": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".icns": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".ini": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".lnk": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".msi": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".sys": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
    ".tmp": os.path.join(FOLDER_DESTINATION, "Text", "Other", "System"),
}

event_handler = Cleanup()
observer = Observer()
observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    observer.stop()


observer.join()
