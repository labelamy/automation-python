import os
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def list_files(directory):
    try:
        files = os.listdir(directory)
        for f in files:
            logging.info(f"Fichier trouvé : {f}")
    except Exception as e:
        logging.error(f"Erreur : {e}")

if __name__ == "__main__":
    list_files("test_folder")