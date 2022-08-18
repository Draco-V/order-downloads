import os
import shutil
from pathlib import Path

home_path = Path.home()
downloads_path = Path(home_path, 'Downloads')
folders = (
    'Text','Videos', 'Audios', 'Images', 'Compressed', 'Executables',
    'Others', 'Documents'
)
text_extensions = ('.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf')
video_extensions = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv')
audio_extensions = ('.mp3', '.wma', '.wav', '.flac')
photo_extensions = ('.jpg', '.png', '.jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg')
compressed_extensions = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
documents_extensions = ('.xlsx', '.pptx', '.csv')
executable_extensions = ('.exe', '.msi', '.app', '.dmg', '.torrent', '.alfredworkflow')



def main():
    pass

if __name__ == '__main__':
    main()