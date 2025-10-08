'''
------------------------------------------------------------- DOCUMENTATION STARTS HERE

[SCRIPT NAME]           GooglePhotosExport-RepairTool.py

[SOURCE REPO @ GITHUB]  https://github.com/azuregray/GooglePhotosExport-RepairTool

[SCRIPT DEPENDENCIES]   Independent Script (No External Script Dependencies);

[DESCRIPTION]           This tool deals with a problem while exporting large data from
                        Google Photos that most of the EXIF & Image Edits data will be
                        stripped to a companion file. This simple interactive tool helps
                        remerge some of the information into the source images files to
                        preserve date-based order while dealing with huge data exports.

[LIBRARIES USED]        os, json, tkinter.filedialog, posixpath, time.sleep

[FUNCTIONS]             coreEngine(workingPath)  -->  MAIN FUNCTION

[NOTE]                  1. Main Section is optimized for better UX, while using with CLI. Just make sure to be a bit patient.
                        2. The script accepts a root directory and works its way down recursively through all folders.
                        3. Its is recommended to have an isolated workspace set for operation which does not contain any other importantfiles.

------------------------------------------------------------- DOCUMENTATION ENDS HERE
'''

def coreEngine(workingPath):
    foundFilesList = os.listdir(workingPath)
    imageFilesList = [file for file in foundFilesList if (not file.endswith('.json')) and (not file.endswith('.py'))]

    processedFilesCount = 0

    for imageFile in imageFilesList:
        for file in foundFilesList:
            if (file.endswith('.json') and ( (file.split(".")[0] + "." + file.split(".")[1]) == imageFile)):
                possibleJsonPath = posixpath.join(workingPath, file)
                with open(possibleJsonPath, 'r') as f:
                    parsedJsonData = json.load(f)
                creationTime = modificationTime = int(parsedJsonData['photoTakenTime']['timestamp'])
                imageFilePath = posixpath.join(workingPath, imageFile)
                os.utime(imageFilePath, (creationTime, modificationTime))
                print(f"✅ Image Data Fixed >> {imageFile}")
                os.remove(possibleJsonPath)
                processedFilesCount += 1
    
    return processedFilesCount


if __name__ == '__main__':
    import os, json, tkinter.filedialog as fd, posixpath
    from time import sleep

    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    
    os.system('cls')
    print(":::::::: Let's Start ::::::::\n\n")
    sleep(1)
    
    os.system('cls')
    print(":::::::: Select a top level directory to start from.. in the prompt that appears now. ::::::::\n\n")
    sleep(0.8)
    
    rootPath = fd.askdirectory(title="Choose Root Directory to start operation.")
    
    os.system('cls')
    print(":::::::: Scanning for accessible folders containing your media... ::::::::\n\n")
    sleep(0.8)
    
    topLevelDirsList = []
    for root, dirsList, filesList in os.walk(rootPath):
        for dirPath in dirsList:
            topLevelDirsList.append(posixpath.join(root, dirPath))
    
    os.system('cls')
    print(":::::::: Scanning Finished ::::::::\n\n")
    sleep(0.8)
    
    input("Press ENTER to start task.")
    os.system('cls')
    
    finalProcessedFilesCounter = 0
    for i, dirPath in enumerate(topLevelDirsList, start=1):
        print(f"Processing Directory {i}/{len(topLevelDirsList)} >> \"{dirPath.split("/")[-1]}\"")
        finalProcessedFilesCounter += coreEngine(dirPath)
        print("\n")
        sleep(0.5)
    
    os.system('cls')
    print(":::::::: Task Completed ::::::::\n\n")
    sleep(0.8)
    print(f"Total Processed Files ->> ({finalProcessedFilesCounter})")
    
    remainingJsonList = [posixpath.join(dirPath, fileName) for dirPath in topLevelDirsList for fileName in os.listdir(dirPath) if fileName.endswith(".json")]
    print(f"\nFailed JSON files remaining ->> ({len(remainingJsonList)})\n\n")
    for pendingJsonFileName in remainingJsonList:
        print(pendingJsonFileName)
    print("\n\n")
    
    if (len(remainingJsonList) > 0):
        optionToRemove = input("Type \"CLEAR\" to delete all unmatched JSON files,\nor just press ENTER to exit (DEFAULT).\n>>> ")
        if optionToRemove.lower() == "clear":
            for jsonFile in remainingJsonList:
                os.remove(jsonFile)
            sleep(1)
            print("\n<---- Remaining JSON files were removed. ---->")
        else:
            sleep(1)
            print("\n<---- Remaining JSON files were not affected. ---->")
    else:
        optionToRemove = input("No unmatched JSON files detected, just press ENTER to exit (DEFAULT).")
    
    sleep(2)
    print("\nNote :: This script has been desgined to catch up by itself\n\tin the next run if by chance it got terminated abruptly.\n")
    
    sleep(1)
    print("\nPlease re-run the script with same top-level directory if that's the case.\n")
    
    sleep(3)
    print("\n\nHope my script was of convenience!\nFind more such interesting things at  >>> github.com/azuregray <<<\n\n")
    sleep(1)

