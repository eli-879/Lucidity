import csv
import json

potential_countries = []
potential_countries1 = ["Germany"]

with open("worldcities.csv", encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        if row[5] == "US" and int(row[9]) > 1000000:
            potential_countries.append(row[0])

def add_data_to_main_file(main_file, new_data, new_data_category):
    with open(main_file, "r") as file:
        data = file.read()
        data = json.loads(data)
        
        
    if new_data_category in data:
        confirm = input("category exists, continue? y/n")
        if confirm == "y":
            replace_or_add = input("replace or add? r/a")
            if replace_or_add == "r":

                data[new_data_category] = new_data

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

add_data_to_main_file("data.txt", potential_countries1, "worldd_items")

