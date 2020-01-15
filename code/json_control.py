import browser_funcs
import json

obj = {"location":"None","query":"None","prev_node":"None","base_locatin":"None"}



def read_data():
    file = open("query.json","r")
    file_data = json.load(file)
    print(file_data)
    browser_funcs.web_driver_setup()
    file.close()

def write_data(data = 'None'):
    file = open("query.json","w")  
    data = json.dumps(obj,indent = 2)
    file.append(data)
    file.close()