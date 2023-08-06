import json


def titlize(s):
    b = []
    for temp in s.split(" "):
        b.append(temp.capitalize())
    return " ".join(b)


uniqued_list = {}

with open("TextFiles/data.txt", "r") as file:
    data = json.load(file)

    for list_of_items in data:
        data[list_of_items] = set(data[list_of_items])
        cleaned_data = list(data[list_of_items])
        print(list_of_items, len(cleaned_data))
        uniqued_list[list_of_items] = [titlize(word) for word in cleaned_data]


with open("TextFiles/data.txt", "w") as file:
    file.write(json.dumps(uniqued_list))
