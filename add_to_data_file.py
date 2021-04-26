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
        print(data)
        
        
    if new_data_category in data:
        confirm = input("category exists, continue? y/n")
        if confirm == "y":
            replace_or_add = input("replace or add? r/a")
            if replace_or_add == "r":

                data[new_data_category] = new_data
                for item in data.items():
                    print(item, "\n")

                with open(main_file, "w") as writing_file:
                    writing_file.write("{\n")
                    counter = 0
                    for k in data.keys():
                        if counter == len(data.keys()) - 1:
                            writing_file.write('"{}" : {}\n'.format(k, json.dumps(data[k])))
                        else:
                            writing_file.write('"{}" : {},\n'.format(k, json.dumps(data[k])))

                        counter = counter + 1

                    writing_file.write("}")

            elif replace_or_add == "a":
                for item in new_data:
                    data[new_data_category].append(item)
                
                with open(main_file, "w") as writing_file:
                    writing_file.write("{\n")
                    counter = 0
                    for k in data.keys():
                        if counter == len(data.keys()) - 1:
                            writing_file.write('"{}" : {}\n'.format(k, json.dumps(data[k])))
                        else:
                            writing_file.write('"{}" : {},\n'.format(k, json.dumps(data[k])))

                        counter = counter + 1

                    writing_file.write("}")
           
        elif confirm == "n":
            pass

    else:
        data[new_data_category] = new_data
        print(data)
        with open(main_file, "w") as writing_file:
            writing_file.write("{\n")
            counter = 0
            for k in data.keys():
                if counter == len(data.keys()) - 1:
                    writing_file.write('"{}" : {}\n'.format(k, json.dumps(data[k])))
                else:
                    writing_file.write('"{}" : {},\n'.format(k, json.dumps(data[k])))

                counter = counter + 1

            writing_file.write("}")


#print(json.dumps(mydict))
#print("\n")

new_data = format_data("objects.txt")

add_data_to_main_file("data.txt", new_data, "object_items")


