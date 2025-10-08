import os

cwd = os.path.dirname(__file__).replace('\\', '/')

for root, dirs, files in os.walk(cwd):
    for filename in files:
        if filename.endswith('.json'):
            print(os.path.join(root, filename))

