import json 
import os

FILE="19_Inventory_systemm/products.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    
    with open(FILE,"r") as f:
        try:
            return json.load(f)
        except:
            return []
        

def save_data(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)