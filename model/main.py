import json
import os

path = ('C:\\Users\\rhdwl\\AppData\\Roaming\\MultiMC\\instances\\1.19.4\\.minecraft\\resourcepacks\\사물 숨바꼭질\\assets\\magic_store\\models\\furnitures\\summer_001\\')

file_list = os.listdir(path)

for file in file_list:
    with open(path + file, 'r') as f:
        json_data = json.load(f)

        print(f"[{file.__str__()}] {json_data}")

        if 'head' not in json_data['display']:
            json_data['display']['head'] = {}

        json_data['display']['head']['rotation'] = [0, 0, 0]
        json_data['display']['head']['translation'] = [0, -30.5, 0]
        json_data['display']['head']['scale'] = [1.6, 1.6, 1.6]

    with open(path + file, 'w', encoding='utf-8') as f1:
        json.dump(json_data, f1)

    with open(path + file, 'r') as f2:
        json_data2 = json.load(f2)

        if 'head' not in json_data2['display']:
            json_data2['display']['head'] = {}

        json_data2['display']['head']['rotation'] = [0, 0, 0]
        json_data2['display']['head']['translation'] = [0, -65, 0]
        json_data2['display']['head']['scale'] = [1.6, 1.6, 1.6]

    new_file_name = os.path.splitext(file)[0] + '_player.json'  # Create a new file name
    with open(path + new_file_name, 'w+', encoding='utf-8') as f3:
        json.dump(json_data2, f3)

if __name__ == '__main__':
    print('1')
