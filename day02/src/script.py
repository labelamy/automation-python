from pathlib import Path
import os
import shutil
import logging

# Crée le dossier logs s'il n'existe pas
os.makedirs("logs", exist_ok=True)

# Configuration logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FILE_CATEGORIES = {
    "images": [".jpg", ".png"],
    "documents": [".pdf", ".docx"],
    "videos": [".mp4", ".mov"],
    "archives": [".zip", ".tar"]
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "others"

def organize_files(source_folder):
    source_path = Path(source_folder)

    if not source_path.exists():
        logging.error(f"Dossier introuvable : {source_folder}")
        return

    for file in source_path.iterdir():

        if file.is_file():

            category = get_category(file.suffix)

            target_folder = source_path / category
            target_folder.mkdir(exist_ok=True)

            target_file = target_folder / file.name

            try:
                shutil.move(str(file), str(target_file))

                logging.info(
                    f"{file.name} déplacé vers {category}"
                )

            except Exception as e:
                logging.error(
                    f"Erreur déplacement {file.name}: {e}"
                )

if __name__ == "__main__":
    organize_files("downloads")