import json
import os

path = ('C:\\Users\\rhdwl\\AppData\\Roaming\\MultiMC\\instances\\1.19.4\\.minecraft\\resourcepacks\\사물 숨바꼭질\\assets\\magic_store\\models\\furnitures\\summer_001\\')

file_list = os.listdir(path)
json_dict = dict()
json_dict["overrides"] = []

custom_model_data = 295

for file in file_list:
    predicate_dict = {"custom_model_data": custom_model_data}
    model_name = f"\"magic_store:furnitures/summer_001/{file.replace('.json', '')}\""
    json_dict["overrides"].append("{ \"predicate\": { \"custom_model_data\": "f"{custom_model_data}"" }, \"model\": "f"{model_name}"" }")
    custom_model_data += 1

if __name__ == '__main__':
    with open('custom_model_data.json', 'w', encoding='utf-8') as make_file:
        json_str = json.dumps(json_dict, indent='\t')
        json_str = json_str.replace('\\"', '"').replace("\"{", "{").replace("}\"", "}")
        make_file.write(json_str)
