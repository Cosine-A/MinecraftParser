import json

json_datas = []
main_dict = dict()


def write_json(type: str, file_dir: str, fileindexc: str):
    chars = []
    repeat_time = 0
    for i2 in range(16):
        char = ""

        for i3 in range(16):
            index = f"{fileindexc}00"
            indexc = "{}".format(hex(int(index, 16) + repeat_time))[2:]
            if char == "":
                char = f"\\u{indexc}"
            else:
                char = f"{char}\\u{indexc}"
            repeat_time += 1
        chars.append(char)

    custom_font = dict()
    custom_font["type"] = type
    custom_font["file"] = file_dir
    custom_font["ascent"] = 0
    custom_font["height"] = 7
    custom_font["chars"] = chars

    main_dict["providers"].append(custom_font)


if __name__ == '__main__':

    fileindex = 'ac'
    main_dict["providers"] = []

    for i in range(44):
        fileindexc = "{}".format(hex(int(fileindex, 16) + i))[2:]
        write_json("bitmap", f"minecraft:font/unicode_page_{fileindexc}.png", fileindexc)
    with open('result.json', 'w', encoding='utf-8') as make_file:
        json.dump(main_dict, make_file, indent="\t", ensure_ascii=False)