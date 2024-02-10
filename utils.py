import json
from pathlib import Path


def extract_route(string):
    return string.split()[1][1:]

def read_file(file_path):
    with open(file_path, 'r') as file:
            content = file.read()
            return content
    
def load_data(filename):
    data_dir = Path("data")
    json_file_path = data_dir / filename
   
    with open(json_file_path, "r") as file:
        data = json.load(file)
        return data
    
def load_template(template_name):
    with open(template_name, "r") as file:
        template_content = file.read()
        return template_content
     