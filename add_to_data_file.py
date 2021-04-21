import json

def format_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        data = data.split(", ")

        return data
        


def add_data_to_main_file(main_file, new_data, new_data_category):
    with open(main_file, "r") as file:
        data = file.read()
        data = json.loads(data)
        
        
    if new_data_category in data:
        confirm = input("category exists, continue? y/n")
        if confirm == "y":
            data[new_data_category] = new_data
            print(data)
            with open(main_file, "w") as writing_file:
                js_data = json.dumps(data)
                writing_file.write(str(js_data))
           
        elif confirm == "n":
            pass

    else:
        data[new_data_category] = new_data
        print(data)
        with open(main_file, "w") as writing_file:
            js_data = json.dumps(data)
            writing_file.write(str(js_data))


#print(json.dumps(mydict))
#print("\n")

new_data = format_data("lolchamps.txt")
add_data_to_main_file("data.txt", new_data, "leaguechamp_items")


