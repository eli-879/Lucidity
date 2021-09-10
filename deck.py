import json
import random
from card import Card

class Deck:
    def __init__(self, filename, screen_width, screen_height, card_assets):
        self.filename = filename
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.card_assets = card_assets

    #Generating Cards
    def import_from_textfile(self, filename):
        with open(filename) as file:
            item_dict = file.read()
            js = json.loads(item_dict)

        return js

    #creates a certain amount of random indexes between two numbers
    def generate_random_indexes(self, size, range1, range2):
        random_indexes = []
        for i in range(size):
            random_indexes.append(random.randrange(range1, range2))

        return random_indexes

    #using previously generated list of random indexes, append the randomly generated item at location of each random index through 0 to 5
    #creates only 1 card
    def generate_item_characteristics(self, rand_indexes, list_of_item_lists):
        items_generated = []
        
        for i in range(len(rand_indexes)):
            items_generated.append(list_of_item_lists[i][rand_indexes[i]])

        return items_generated

    #ensures that there are no repeats - pops only 1 items per list to ensure no index errors
    def delete_items(self, rand_indexes, list_of_item_lists):
        for i in range(len(rand_indexes)):
            list_of_item_lists[i].pop(rand_indexes[i])

    def get_end_range(self, list_of_item_lists):
        #finding shortest category list and making deck length according to that length
        min = 99999
        shortest_list = 0
        for i in range(len(list_of_item_lists)):
            if len(list_of_item_lists[i]) < min:
                min = len(list_of_item_lists[i])
                shortest_list = i
        
        return min, shortest_list

    def create_cards(self, list_of_item_lists):
        list_of_card_objects = []
        items_list = list_of_item_lists

        #getting shortest list length
        num_cards, shortest_list = self.get_end_range(list_of_item_lists)

        #creating cards
        for i in range(num_cards):
            rand_indexes_for_items = []
            for j in range(len(list_of_item_lists)):                            #generate random indexes for card items
                
                rand_index = random.randrange(0, len(list_of_item_lists[j]))
                rand_indexes_for_items.append(rand_index)
                
            list_of_items = self.generate_item_characteristics(rand_indexes_for_items, items_list)
            self.delete_items(rand_indexes_for_items, items_list)

            #getting a random category for the ace
            rand_index_for_ace = self.generate_random_indexes(1, 0, 6)
            card = Card(list_of_items, rand_index_for_ace, self.screen_width, self.screen_height, self.card_assets)
            list_of_card_objects.append(card)

        return list_of_card_objects

    def generate_deck(self): 

        # Importing data from files into lists
        item_dict = self.import_from_textfile("TextFiles/data.txt")

        #different categories
        people_list = item_dict["person_items"]
        world_list = item_dict["world_items"]
        object_list = item_dict["object_items"]
        action_list = item_dict["action_items"]
        nature_list = item_dict["nature_items"]
        random_list = item_dict["random_items"]
        leaguechamp_list = item_dict["leaguechamp_items"]
        pokemon_list = item_dict["pokemon_items"]

        #the lists that will be used for each card
        list_of_item_lists = [people_list, world_list, object_list, nature_list, action_list, leaguechamp_list]

        deck_of_cards = self.create_cards(list_of_item_lists)
        open_card = []

        return deck_of_cards