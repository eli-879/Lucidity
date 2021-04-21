import pygame
import random
import json

pygame.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Articulate!")
FPS = 60
clock = pygame.time.Clock()
word_font = pygame.font.SysFont("calibri", 60)

BG = pygame.image.load("background.jpg")
CARD_BACK = pygame.image.load("card_back.jpg")
CARD_BACK = pygame.transform.scale(CARD_BACK, (400, 300))




class Card():
    
    def __init__(self, list_of_items):
        
        self.__up = False
        self.__down = True
        self.__HEIGHT = 300
        self.__WIDTH = 400
        self.__xpos = (WIDTH - self.__WIDTH) / 2
        self.__ypos_fdown = (HEIGHT - (self.__HEIGHT) * 2) / 3
        self.__ypos_fup =  (2 * ((HEIGHT - (self.__HEIGHT) * 2) / 3)) + self.__HEIGHT
        self.__card_back = CARD_BACK
        self.__mask = self.__card_back.get_rect()
        self.__people_item = list_of_items[0]
        self.__world_item = list_of_items[1]
        self.__object_item = list_of_items[2]
        self.__action_item = list_of_items[3]
        self.__nature_item = list_of_items[4]
        self.__random_item = list_of_items[5]
        self.__list_of_items = [self.__people_item, self.__world_item, self.__object_item, self.__action_item, self.__nature_item, self.__random_item]
        self.__people_item = None
        self.__world_item = None
        self.__object_item = None
        self.__nature_item = None
        self.__random_item = None

    def __str__(self):
        return str(self.__list_of_items)

    def draw(self, window):
        if self.__up == True:
            window.blit(self.__card_back, (self.__xpos, self.__ypos_fup))
        elif self.__down == True:
            window.blit(self.__card_back, (self.__xpos, self.__ypos_fdown))

    def detect_collision(self):
        pass

    def get_x_coords(self):
        return (self.__xpos, self.__xpos + self.__WIDTH)

    def get_y_coords(self):
        return (self.__ypos, self.__pos + self.__HEIGHT)

    def set_up_true(self):
        self.__up = True
        self.__down = False

    def set_down_true(self):
        self.__up = False
        self.__down = True


class Deck:

    def __init__(self, list_of_cards):
        self.__list_of_cards = list_of_cards
        self.__top_card = []
        self.__used_cards = []

    def draw(self, window):
        self.__top_card.draw()





def import_from_textfile(filename):
    with open(filename) as file:
        item_dict = file.read()
        js = json.loads(item_dict)

    return js

def generate_random_indexes(size, range1, range2):
    random_indexes = []
    for i in range(size):
        random_indexes.append(random.randrange(range1, range2))

    return random_indexes

def generate_item_characteristics(rand_indexes, list_of_item_lists):
    items_generated = []

    for i in range(len(rand_indexes)):
        items_generated.append(list_of_item_lists[i][rand_indexes[i]])

    return items_generated

def delete_items(rand_indexes, list_of_item_lists):
    for i in range(len(rand_indexes)):
        list_of_item_lists[i].pop(rand_indexes[i])

def create_cards(list_of_item_lists):
    list_of_card_objects = []
    items_list = list_of_item_lists
    num_cards = len(list_of_item_lists[0])

    for i in range(num_cards):
        end_range = len(items_list[0])
        rand_indexes = generate_random_indexes(6, 0, end_range)                 #generate random indexes for card items
        list_of_items = generate_item_characteristics(rand_indexes, items_list)
        delete_items(rand_indexes, items_list)
        card = Card(list_of_items)
        list_of_card_objects.append(card)

    return list_of_card_objects

def main(): 
    
    # Importing data from files into lists
    item_dict = import_from_textfile("data.txt")
    people_list = item_dict["person_items"]
    world_list = item_dict["world_items"]
    object_list = item_dict["object_items"]
    action_list = item_dict["action_items"]
    nature_list = item_dict["nature_items"]
    random_list = item_dict["random_items"]

    list_of_item_lists = [people_list, world_list, object_list, action_list, nature_list, random_list]

    deck_of_cards = create_cards(list_of_item_lists)
    open_card = []


    for item in (deck_of_cards):
        print(item)


    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                print(x_pos, y_pos)
                if (deck_of_cards[0].get_x_coords()[0] <= x_pos <= deck_of_cards[0].get_x_coords()[1]):
                    deck_of_cards[0].set_up_true()
                    




        
        WIN.blit(BG, (0,0))

        deck_of_cards[0].draw(WIN)


        pygame.display.update()


    pygame.quit()

    

main()

    
    






