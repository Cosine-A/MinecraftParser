import requests
from bs4 import BeautifulSoup
import re

versions = ["1.17.1", "1.18", "1.18.1", "1.18.2", "1.19", "1.19.1", "1.19.2", "1.19.3", "1.19.4", "1.20", "1.20.1", "1.20.2"]

functions = []

mojang_pattern = r'Mojang ([a-zA-Z0-9_]+)(.*+)'
forge_pattern = r'Searge \(Forge\) ([a-zA-Z0-9_]+)(.*+)'

search_function_name = "contains"
max_argument_size = 1

def printFunction(version):
    r = requests.get(f'https://nms.screamingsandals.org/{version}/net/minecraft/nbt/CompoundTag.html')
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    uls = soup.find_all("ul", {"class": "list-unstyled"})

    for loop in range(uls.__len__() - 1):
        lis = uls[loop].findAll("li")

        mojang_li = next(filter(lambda li: 'Mojang' in li.text, lis), None).text
        forge_li = next(filter(lambda li: 'Forge' in li.text, lis), None).text

        mojang_match = re.search(mojang_pattern, mojang_li)
        forge_match = re.search(forge_pattern, forge_li)

        if mojang_match:
            mojang_function_name = mojang_match.group(1)
            if mojang_function_name != search_function_name:
                continue
            mojang_function_argument_text = mojang_match.group(2)
            mojang_function_arguments = mojang_function_argument_text.split(", ")
            if len(mojang_function_arguments) > max_argument_size:
                continue
            mojang_text = f"{mojang_function_name}{mojang_match.group(2)}"
        else:
            continue
        if forge_match:
            forge_text = f"{forge_match.group(1)}{forge_match.group(2)}"
        else:
            continue
        functions.append(forge_text)
        print(f"[{version}] {mojang_text}")
        print(f"         └ {forge_text}")
        print("")

#printFunction("1.17.1")
for version in versions:
    printFunction(version)

print("")
if all(x == functions[0] for x in functions):
    print("모든 요소가 같습니다.")
else:
    print("요소가 같지 않습니다.")

def printFunction2(version):
    r = requests.get(f'https://nms.screamingsandals.org/{version}/net/minecraft/nbt/CompoundTag.html')
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
            functions.append(function)
            print(f"[{version}] {function}")
            print("")