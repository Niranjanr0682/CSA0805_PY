#in function.py
import os


def load_data():
    global resources
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            resources = json.load(file)


#in interface.py
#import the loaddata and call the function in main
