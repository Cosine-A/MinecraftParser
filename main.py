import requests
from bs4 import BeautifulSoup
import re

versions = ["1.17.1", "1.18", "1.18.1", "1.18.2", "1.19", "1.19.1", "1.19.2", "1.19.3", "1.19.4", "1.20", "1.20.1",
            "1.20.2"]

obfuscated_functions = []
forge_functions = []

mojang_pattern = r'Mojang ([a-zA-Z0-9_]+)(.*+)'
obfuscated_pattern = r'Obfuscated ([a-zA-Z0-9_]+)(.*+)'
forge_pattern = r'Searge \(Forge\) ([a-zA-Z0-9_]+)(.*+)'

search_function_name = "getDescriptionId"
argument_size = 1


def printFunction(version_text):
    r = requests.get(f'https://nms.screamingsandals.org/{version_text}/net/minecraft/world/item/Item.html')
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    uls = soup.find_all("ul", {"class": "list-unstyled"})

    for loop in range(uls.__len__() - 1):
        lis = uls[loop].findAll("li")

        mojang_li = next(filter(lambda li: 'Mojang' in li.text, lis), None).text
        obfuscated_li = next(filter(lambda li: 'Obfuscated' in li.text, lis), None).text
        forge_li = next(filter(lambda li: 'Forge' in li.text, lis), None).text

        mojang_match = re.search(mojang_pattern, mojang_li)
        obfuscated_match = re.search(obfuscated_pattern, obfuscated_li)
        forge_match = re.search(forge_pattern, forge_li)

        if mojang_match:
            mojang_function_name = mojang_match.group(1)
            if mojang_function_name != search_function_name:
                continue
            mojang_function_argument_text = mojang_match.group(2)
            mojang_function_arguments = mojang_function_argument_text.split(", ")
            if "()" in mojang_function_argument_text and argument_size == 1:
                continue
            if len(mojang_function_arguments) > argument_size:
                continue
            mojang_text = f"{mojang_function_name}{mojang_match.group(2)}"
        else:
            continue
        if obfuscated_match:
            obfuscated_function_name = obfuscated_match.group(1)
            obfuscated_functions.append(obfuscated_function_name)
            obfuscated_text = f"{obfuscated_function_name}{obfuscated_match.group(2)}"
        else:
            continue
        if forge_match:
            forge_function_name = forge_match.group(1)
            forge_functions.append(forge_function_name)
            forge_text = f"{forge_function_name}{forge_match.group(2)}"
        else:
            continue
        print(f"[{version}] {mojang_text}")
        print(f"         └ {obfuscated_text}")
        print(f"         └ {forge_text}")
        print("")


# printFunction("1.17.1")
for version in versions:
    printFunction(version)


def isEveryEqual(input_list):
    if all(x == input_list[0] for x in input_list):
        return True
    else:
        return False


print("")
if isEveryEqual(obfuscated_functions):
    print("[Obfuscated] 모든 요소가 같습니다.")
else:
    print("[Obfuscated] 모든 요소가 같지 않습니다.")
if isEveryEqual(forge_functions):
    print("[Forge] 모든 요소가 같습니다.")
else:
    print("[Forge] 모든 요소가 같지 않습니다.")


def printFunction2(version2):
    r = requests.get(f'https://nms.screamingsandals.org/{version2}/net/minecraft/nbt/CompoundTag.html')
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    lis = soup.findAll("li")

    mojang_function = "remove"
    forge_function = "m_128473_"

    mojang_pattern = r'Mojang ([a-zA-Z0-9_]+)'
    forge_pattern = r'Searge \(Forge\) ([a-zA-Z0-9_]+)'

    for li in lis:
        text = li.text
        mojang_match = re.search(mojang_pattern, text)
        forge_match = re.search(forge_pattern, text)
        if mojang_match:
            function = mojang_match.group(1)
            if mojang_function != function:
                continue
            print(f"[{version}] {function}")
        if forge_match:
            function = forge_match.group(1)
            if forge_function != function:
                continue
            forge_functions.append(function)
            print(f"[{version}] {function}")
            print("")
