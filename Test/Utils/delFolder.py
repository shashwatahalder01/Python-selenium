import shutil
import os
from pathlib import Path

# Delete folder path
baseDir = Path(__file__).resolve().parent.parent
dirName = "ReportAllure"
dirPath = os.path.join(baseDir, dirName)
print(dirPath)


def delfolder(folderName):
    # Delete folder
    try:
        shutil.rmtree(folderName)
    except OSError as e:
        print("Error: %s : %s" % (dirPath, e.strerror))


delfolder(dirPath)

