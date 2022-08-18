from genericpath import isdir
import os
import shutil
from pathlib import Path
from tkinter import image_names

home_path = Path.home()
downloads_path = Path(home_path, "Downloads")
folders = (
    "Text",
    "Videos",
    "Audios",
    "Images",
    "Compressed",
    "Executables",
    "Others",
    "Documents",
)
text_extensions = (".txt", ".doc", ".docx", "pptx", ".odf", ".docm", ".pdf")
video_extensions = (".mov", ".mp4", ".avi", ".mkv", ".mkv", ".flv", ".wmv")
audio_extensions = (".mp3", ".wma", ".wav", ".flac")
photo_extensions = (
    ".jpg",
    ".png",
    ".jpeg",
    ".gif",
    ".tiff",
    ".psd",
    ".bmp",
    ".ico",
    ".svg",
)
compressed_extensions = (".zip", ".rar", ".rar5", ".7z", ".ace", ".gz")
documents_extensions = (".xlsx", ".pptx", ".csv")
executable_extensions = (".exe", ".msi", ".app", ".dmg", ".torrent", ".alfredworkflow")


def user_option():
    while True:
        option = input(
            "Do you want the script to create the missing folders? (y/n): "
        ).lower()
        if option != "n" and option != "y":
            print("Please type a given option. ")
        else:
            if option == "y":
                create_folders()
                localize_files()
            else:
                print(
                    "This script need to create the folders in order to organize all the files.\nType e to exit."
                )
            break


def create_folders():
    for folder in folders:
        new_folder = os.path.join(downloads_path, folder)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)


def localize_files():
    for file in Path.glob(downloads_path, "*"):
        if not file.name in folders:
            print(file)
            move_file(file)


def move_file(file: Path):
    if os.path.isdir(file):
        shutil.move(file, Path(downloads_path, "Others"))
    else:
        if file.suffix in photo_extensions:
            shutil.move(file, Path(downloads_path, "Images"))
        elif file.suffix in text_extensions:
            shutil.move(file, Path(downloads_path, "Text"))
        elif file.suffix in video_extensions:
            shutil.move(file, Path(downloads_path, "Videos"))
        elif file.suffix in audio_extensions:
            shutil.move(file, Path(downloads_path, "Audio"))
        elif file.suffix in compressed_extensions:
            shutil.move(file, Path(downloads_path, "Compressed"))
        elif file.suffix in documents_extensions:
            shutil.move(file, Path(downloads_path, "Documents"))
        elif file.suffix in executable_extensions:
            shutil.move(file, Path(downloads_path, "Executables"))
        elif file.suffix == "":
            shutil.move(file, Path(downloads_path, "Others"))


def main():
    user_option()


if __name__ == "__main__":
    main()
