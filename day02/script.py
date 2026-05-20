import os
import shutil

def organize(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".jpg"):
            os.makedirs("images", exist_ok=True)
            shutil.move(path, f"images/{file}")

        elif file.endswith(".txt"):
            os.makedirs("documents", exist_ok=True)
            shutil.move(path, f"documents/{file}")

        elif file.endswith(".pdf"):
            os.makedirs("pdfs", exist_ok=True)
            shutil.move(path, f"pdfs/{file}")

organize("test_folder")