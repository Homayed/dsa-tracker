import json
import os

#defining json file
DATA_FILE = "data.json"

#making load_data function to load the data
def load_data():
    if not os.path.exists(DATA_FILE): # to check if the file or folder exists
        return []
    with open(DATA_FILE,"r") as f: #read data
        try:
            return json.load(f)#reads data and turn it into a python dict
        except json.JSONDecodeError:
            return [] #handles the broken file error

#making save_data function to save the data
def save_data(data):
    with open(DATA_FILE,"w") as f: #write data
        json.dump(data,f,indent = 4) #writes to a file