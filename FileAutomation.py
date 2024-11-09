from os import scandir, rename
from os.path import splitext, exists, join, isfile, isdir
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define source and destination directories
source_dir = "/home/jackpk/Downloads"
dest_dir_sfx = "/home/jackpk/Downloads"
dest_dir_music = "/home/jackpk/Music"
dest_dir_video = "/home/jackpk/Videos"
dest_dir_image = "/home/jackpk/Pictures"
dest_dir_documents = "/home/jackpk/Documents"
dest_dir_github = "/home/jackpk/GitHub"

# Define file type extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp"]
video_extensions = [".mp4", ".avi", ".mov", ".wmv"]
audio_extensions = [".mp3", ".flac", ".wav"]
document_extensions = [".pdf", ".docx", ".xlsx", ".pptx"]


def make_unique(dest, name):
    """Generate a unique file name if the file already exists in the destination directory."""
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    """Move file to the specified destination folder, with existence check."""
    if not exists(entry):  # Check if the file still exists before moving
        logging.warning(f"File {entry} not found. Skipping move.")
        return

    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)
    try:
        move(entry, dest)
        logging.info(f"Moved file: {name} to {dest}")
    except FileNotFoundError as e:
        logging.error(f"File {entry} not found during move: {e}")


def check_audio_files(entry, name):
    for audio_extension in audio_extensions:
        if name.lower().endswith(audio_extension):
            dest = dest_dir_sfx if entry.stat().st_size < 10_000_000 or "SFX" in name else dest_dir_music
            move_file(dest, entry, name)
            break


def check_video_files(entry, name):
    for video_extension in video_extensions:
        if name.lower().endswith(video_extension):
            move_file(dest_dir_video, entry, name)
            break


def check_document_files(entry, name):
    for document_extension in document_extensions:
        if name.lower().endswith(document_extension):
            move_file(dest_dir_documents, entry, name)
            break


def check_image_files(entry, name):
    for image_extension in image_extensions:
        if name.lower().endswith(image_extension):
            move_file(dest_dir_image, entry, name)
            break


def check_github_files(entry, name):
    """Move .git files and folders to the GitHub directory."""
    if ".git" in name:
        move_file(dest_dir_github, entry, name)


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Only handle modified files, not directories
        if event.is_directory:
            return
        name = event.src_path
        entry_name = name.split("/")[-1]  # Extract file name from the full path

        # Check file extensions to decide the destination folder
        check_github_files(name, entry_name)
        check_audio_files(name, entry_name)
        check_video_files(name, entry_name)
        check_image_files(name, entry_name)
        check_document_files(name, entry_name)


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir  # Set the directory to be monitored
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
