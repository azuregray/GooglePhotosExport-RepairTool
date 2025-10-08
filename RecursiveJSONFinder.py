'''
------------------------------------------------------------- DOCUMENTATION STARTS HERE

[SCRIPT NAME]           RecursiveJSONFinder.py

[SOURCE REPO @ GITHUB]  https://github.com/azuregray/GooglePhotosExport-RepairTool

[DESCRIPTION]           This is just a companion script with the main script "GooglePhotosExport-RepairTool.py".
                        Goal of this script is to recursively, hierarchically find & list any JSON files left
                        behind by the main script. Yet can also be used as a general script to find and list
                        all JSON full file paths recoursively starting with a root parent directory.

[LIBRARIES USED]        os, json, tkinter.filedialog, posixpath, time.sleep

[NOTE]                  1. Main Section is not included for obvious reasons.
                        2. The script assumes the current script directory location as the root directory and works its way down recursively throughout.
                        3. Its is safe to have any other file types, as the process is essentially just gathering JSON files and displaying full paths for the same.

------------------------------------------------------------- DOCUMENTATION ENDS HERE
'''

import os

cwd = os.path.dirname(__file__).replace('\\', '/')

for root, dirs, files in os.walk(cwd):
    for filename in files:
        if filename.endswith('.json'):
            print(os.path.join(root, filename))