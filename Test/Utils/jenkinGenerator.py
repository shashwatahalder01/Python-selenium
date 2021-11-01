import os
from pathlib import Path

fileContainer = "TestCase/"
fileContainerPath = Path(__file__).parent.parent / fileContainer
pathRootFolderName = 'Test'


# Get absolute file path
def getAbsoluteFilePath(fileContainer):
    absoluteFilePathList = []
    for root, dirs, files in os.walk(fileContainer):
        for file in files:
            if file.startswith("__init__"):
                continue
            if file.endswith(".py"):
                f = os.path.join(root, file)
                absoluteFilePathList.append(f)
    return absoluteFilePathList


# Get path from chosen root
def getFilePathFromChosenRoot(absoluteFilePathList):
    formattedFilePathList = []
    for filePath in absoluteFilePathList:
        formattedFilePath = str(filePath).split(f'{pathRootFolderName}/')[-1]
        formattedFilePathList.append(formattedFilePath)
    return formattedFilePathList


#  Get File name
def getFileName(absoluteFilePathList):
    originalFileNameList = []
    for fileName in absoluteFilePathList:
        originalFileName = str(fileName).split('/')[-1].rsplit('.py')[0]
        originalFileNameList.append(originalFileName)
    return originalFileNameList


#  Get Reformatted file name
def getFormattedFileName(absoluteFilePathList):
    formattedFileList = []
    for fileName in absoluteFilePathList:
        originalFileName = str(fileName).split('/')[-1].rsplit('.py')[0]
        formattedFileName = originalFileName.replace('_', ' ')
        formattedFileName = formattedFileName.title()
        formattedFileName = formattedFileName.split(' ')
        formattedFileName = f"{formattedFileName[0]} {' '.join(formattedFileName[3:])}"
        # print(formattedFileName)
        formattedFileList.append(formattedFileName)
    return formattedFileList


AbsPath = getAbsoluteFilePath(fileContainerPath)
formattedPath = getFilePathFromChosenRoot(AbsPath)
formattedFileName = getFormattedFileName(formattedPath)


# for filepath in formattedPath:
#     print(filepath)
#
# for filename in formattedFileName:
#     print(filename)


jenkinConfiguration = []
for i in range(len(formattedPath)):
    f = f"        '[{formattedFileName[i]}]': '{formattedPath[i]}',\n"
    jenkinConfiguration.append(f)
#     print(f)
# print(jenkinConfiguration)


file = Path(__file__).parent / 'JenkinsfileSkeleton'
file1 = Path(__file__).parent.parent.parent / 'Jenkinsfile'
with open(file) as f:
    lines = f.readlines()
    # print(lines)
    for i in range(len(jenkinConfiguration)):
        lines.insert(7+i, jenkinConfiguration[i])
    # print(lines)
    print(*lines, sep="\n")

with open(file1, "w") as f2:
    f2.writelines(lines)