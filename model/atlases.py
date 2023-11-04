import json
import os

path = ('C:\\Users\\rhdwl\\AppData\\Roaming\\MultiMC\\instances\\1.19.4\\.minecraft\\resourcepacks\\사물 숨바꼭질\\assets\\magic_store\\textures\\furnitures\\summer_001\\')

file_list = os.listdir(path)
json_dict = dict()
json_dict["sources"] = []

for file in file_list:
    model_name = f"\"magic_store:furnitures/summer_001/{file.replace('.png', '')}\""
    json_dict["sources"].append("{ \"type\": \"single\", \"resource\": "f"{model_name}"" }")

if __name__ == '__main__':
    with open('atlases.json', 'w', encoding='utf-8') as make_file:
        json_str = json.dumps(json_dict, indent='\t')
        json_str = json_str.replace('\\"', '"').replace("\"{", "{").replace("}\"", "}")
        make_file.write(json_str)
