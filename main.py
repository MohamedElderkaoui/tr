import os
from pathlib import Path
from PIL import Image


def get_downloads_folder() -> Path:
    return Path(os.path.expanduser("~/Downloads"))


def get_pictures_folder() -> Path:
    return Path(os.path.expanduser("~/Pictures"))

def get_pdf_folder() -> Path:
    return Path(os.path.expanduser("~/Documentos"))


def compress_image(image: Image.Image, filename: str, output_folder: Path) -> None:
    compressed_filename = f"compressed_{filename}"
    image.save(output_folder / compressed_filename, optimize=True, quality=60)


def move_file(file_path: Path, destination_folder: Path) -> None:
    destination_folder.mkdir(parents=True, exist_ok=True)
    file_path.rename(destination_folder / file_path.name)


def handle_image_file(file_path: Path) -> None:
    extension = file_path.suffix.lower()
    if extension in [".jpg", ".jpeg", ".png"]:
        with Image.open(file_path) as image:
            compress_image(image, file_path.name, get_pictures_folder())
        file_path.unlink()


def handle_music_file(file_path: Path) -> None:
    extension = file_path.suffix.lower()
    if extension == ".mp3":
        move_file(file_path, get_music_folder())


def get_music_folder() -> Path:
    return Path(os.path.expanduser("~/Music"))


# to pdf or docs
def handle_pdf_file(file_path: Path) -> None:
    extension = file_path.suffix.lower()
    if extension == ".pdf" or extension == ".docs":
        move_file(file_path, get_pdf_folder())  # noqa: F823

def get_pdf_folder() -> Path:
    return Path(os.path.expanduser("C:\Users\ACER i7 10TH\Documents"))


def main() -> None:
    downloads_folder = get_downloads_folder()
    for file_path in downloads_folder.iterdir():
        handle_image_file(file_path)
        handle_music_file(file_path)
        handle_pdf_file(file_path)


if __name__ == "__main__":
    main()
