import os
import smtplib
import shutil
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime


# from runconfiguration import linux

# Read counter
def read_counter():
    # read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    return data


# Read and Update counter
def readAndUpdateCounter():
    # read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # update counter
    newCounter = str(data + 1)
    # write new counter
    f.seek(0)
    f.write(newCounter)
    f.truncate()
    f.close()
    return newCounter


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# Delete Folder and its content except last n number of dirs
def del_dir(num_of_dir):
    basedir = Path(__file__).resolve().parent.parent
    dirName = "ReportAllure"
    dirPath = os.path.join(basedir, dirName)
    # print(dirPath)
    # dirList = [f for f in sorted(os.listdir(dirPath))]
    dirList = [os.path.join(dirPath, f) for f in sorted(os.listdir(dirPath))]
    dirList = dirList[:len(dirList) - num_of_dir]
    # print(dirList)
    for folder in dirList:
        try:
            shutil.rmtree(folder)
            # print('delete: ' + delDir)
        except OSError as e:
            print("Error: %s : %s" % (folder, e.strerror))
        # print('dir deleted')


# Delete file except last n number of files
def del_file(num_of_file):
    basedir = Path(__file__).resolve().parent.parent
    dirName = "ReportHtml"
    dirPath = os.path.join(basedir, dirName)
    fileList = [os.path.join(dirPath, f) for f in sorted(os.listdir(dirPath))]
    fileList = fileList[:len(fileList) - num_of_file]
    # print(fileList)
    for file in fileList:
        os.remove(file)


def keep_reports(number):
    del_dir(number)
    del_file(number)
