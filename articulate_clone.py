import pygame
import random
import json

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Articulate!")
FPS = 60
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
word_font = pygame.font.SysFont("calibri", 20)

BG = pygame.image.load("background.jpg")
CARD_BACK = pygame.image.load("card_back.jpg")
CARD_FRONT = pygame.image.load("card_front.png")
CARD_FRONT = pygame.transform.scale(CARD_FRONT, (400, 300))
CARD_BACK = pygame.transform.scale(CARD_BACK, (400, 300))
SPADES = pygame.image.load("spades.png")
SPADES = pygame.transform.scale(SPADES, (30, 30))


class Card:
    
    def __init__(self, list_of_items, ace_index):
        
        self.__up = False
        self.__down = True
        self.__HEIGHT = 300
        self.__WIDTH = 400
        self.__xpos = (WIDTH - self.__WIDTH) / 2
        self.__ypos_fdown = (HEIGHT - (self.__HEIGHT) * 2) / 3
        self.__ypos_fup =  (2 * ((HEIGHT - (self.__HEIGHT) * 2) / 3)) + self.__HEIGHT
        self.__card_back = CARD_BACK
        self.__card_front = CARD_FRONT
        self.__ace = SPADES
        self.__mask = self.__card_back.get_rect()

        self.__people_item = list_of_items[0]
        self.__world_item = list_of_items[1]
        self.__object_item = list_of_items[2]
        self.__action_item = list_of_items[3]
        self.__nature_item = list_of_items[4]
        self.__random_item = list_of_items[5]
        self.__ace_index = ace_index[0]
        self.__list_of_items = [self.__people_item, self.__world_item, self.__object_item, self.__action_item, self.__nature_item, self.__random_item]
        
    def __str__(self):
        string = str(self.__list_of_items) + " Ace Category: " + str(self.__ace_index)
        return string

    def draw(self, window):
        if self.__up == True:
            window.blit(self.__card_front, (self.__xpos, self.__ypos_fup))
            category_0 = word_font.render(self.__list_of_items[0], 1, BLACK)
            category_1 = word_font.render(self.__list_of_items[1], 1, BLACK)
            category_2 = word_font.render(self.__list_of_items[2], 1, BLACK)
            category_3 = word_font.render(self.__list_of_items[3], 1, BLACK)
            category_4 = word_font.render(self.__list_of_items[4], 1, BLACK)
            category_5 = word_font.render(self.__list_of_items[5], 1, BLACK)

            list_of_cat = [category_0, category_1, category_2, category_3, category_4, category_5]

            for i in range(len(list_of_cat)):
                initial_y_pos = self.__ypos_fup + 41 - list_of_cat[i].get_height()
                y_gaps = 7.5 * i
                center_box = ((36 - list_of_cat[i].get_height()) / 2) + ((i) * 36)
                window.blit(list_of_cat[i], (self.__xpos + 60, initial_y_pos + center_box + y_gaps))

                if i == self.__ace_index:
                    window.blit(self.__ace, (self.__xpos + 370 - 17.4, initial_y_pos + center_box + y_gaps - 5))
       
        elif self.__down == True:
            window.blit(self.__card_back, (self.__xpos, self.__ypos_fdown))

    def detect_collision(self):
        pass

    def get_x_coords(self):
        return (self.__xpos, self.__xpos + self.__WIDTH)

    def get_y_coords(self):
        return (self.__ypos_fdown, self.__ypos_fdown + self.__HEIGHT)

    def set_up_true(self):
        self.__up = True
        self.__down = False

    def set_down_true(self):
        self.__up = False
        self.__down = True

class Button:

    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.__rect = pygame.Rect(rect)
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__command = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center = self.__rect.center)
        #self.__text = text

    def process_kwargs(self, kwargs):
        settings = {
            "color"               :pygame.Color("red"),
            "text"                :"Start Round",
            "font"                :pygame.font.SysFont("Arial", 16),
            "hover_color"         :(200,0,0),
            "font_color"          :pygame.Color("white")       
            }

        #can pass dictionary with many new settings into kwargs to change it

        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))

        self.__dict__.update(settings)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.__rect.collidepoint(event.pos):
            self.__command()

    def is_hovering(self):
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.__image.fill(self.hover_color)
        else:
            self.__image.fill(self.color)
            
        surf.blit(self.__image, self.__rect)
        surf.blit(self.text, self.text_rect)

class Timer:

    def __init__(self, rect, seconds, beep):
        self.__rect = pygame.Rect(rect)
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__counter = seconds
        self.__counter_fixed = seconds
        self.__text = word_font.render(str(self.__counter), True, (0,128,0))
        self.__text_rect = self.__text.get_rect(center = self.__rect.center)
        self.__timer_event = pygame.USEREVENT + 1
        self.__timer = pygame.time.set_timer(self.__timer_event, 1000)
        self.__beep = beep

    def get_timer_event(self):
        return self.__timer_event

    def reduce_counter(self, open_card, deck_of_cards):
        self.__counter -= 1
        self.__text = word_font.render(str(self.__counter), True, (0,128,0))

        if self.__counter == 10:
            pygame.mixer.Sound.play(self.__beep)

        if self.__counter == 0:
            pygame.mixer.Sound.play(self.__beep, loops=2)
            

        if self.__counter <= 0:
            print("OVER!")
            self.__timer = pygame.time.set_timer(self.__timer_event, 0)
            if len(open_card) >= 1:
                open_card[0].set_down_true()              
                open_card.pop(0)

                print("Cards in deck")
                for item in deck_of_cards:
                    print(item)

                print("Card in hand")
                
            else:
                pass

    def reset(self):
        print("D")
        self.__counter = self.__counter_fixed + 1
        self.__timer = pygame.time.set_timer(self.__timer_event, 1000)

    def draw(self, window):
        window.blit(self.__image, self.__rect)
        window.blit(self.__text, self.__text_rect )



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

def get_end_range(list_of_item_lists):
    min = 99999
    shortest_list = 0
    for i in range(len(list_of_item_lists)):
        if len(list_of_item_lists[i]) < min:
            min = len(list_of_item_lists[i])
            shortest_lst = i
    return min, shortest_list

def create_cards(list_of_item_lists):
    list_of_card_objects = []
    items_list = list_of_item_lists
    num_cards, shortest_list = get_end_range(list_of_item_lists)
    print(num_cards, "- number of cards")
    print(items_list[shortest_list])

    for i in range(num_cards):
        rand_indexes_for_items = []
        for j in range(len(list_of_item_lists)):                            #generate random indexes for card items
            rand_index = random.randrange(0, len(list_of_item_lists[j]))
            rand_indexes_for_items.append(rand_index)
            
        list_of_items = generate_item_characteristics(rand_indexes_for_items, items_list)
        delete_items(rand_indexes_for_items, items_list)
        rand_index_for_ace = generate_random_indexes(1, 0, 6)
        card = Card(list_of_items, rand_index_for_ace)
        list_of_card_objects.append(card)

    return list_of_card_objects

def draw_hand(window, hand_list):
    if len(hand_list) > 0:
        hand_list[0].draw(window)

def draw(window, deck_of_cards, open_hand, btn, timer):
    WIN.blit(BG, (0,0))

    deck_of_cards[0].draw(WIN)
    draw_hand(WIN, open_hand)
    btn.draw(WIN)
    timer.draw(WIN)


def main(): 
    
    # Importing data from files into lists
    item_dict = import_from_textfile("data.txt")
    people_list = item_dict["person_items"]
    world_list = item_dict["world_items"]
    object_list = item_dict["object_items"]
    action_list = item_dict["action_items"]
    nature_list = item_dict["nature_items"]
    random_list = item_dict["random_items"]
    leaguechamp_list = item_dict["leaguechamp_items"]
    pokemon_list = item_dict["pokemon_items"]

    list_of_item_lists = [people_list, world_list, object_list, nature_list, pokemon_list, leaguechamp_list]

    deck_of_cards = create_cards(list_of_item_lists)
    open_card = []

    ambient_music = pygame.mixer.Sound("jazz.mp3")
    ambient_music.set_volume(0.1)
    pygame.mixer.Sound.play(ambient_music, loops=-1)

    beep = pygame.mixer.Sound("beep.wav")

    timer = Timer(rect=(100, 166.66, 200, 25), seconds=15, beep = beep)
    btn = Button(rect=(100, 66.66, 200, 25), command = timer.reset)

    


    run = True


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():                    #check if exit is clicked
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):                    #check if mouse is pressed
                x_pos, y_pos = pygame.mouse.get_pos()
                print(x_pos, y_pos)
                
                if (deck_of_cards[0].get_x_coords()[0] <= x_pos <= deck_of_cards[0].get_x_coords()[1]) and \
                    (deck_of_cards[0].get_y_coords()[0] <= y_pos <= deck_of_cards[0].get_y_coords()[1]) \
                    or ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):                 #if mouse click loc is within card range, go to next card
                    
                    if len(open_card) == 0:                 #if no cards are face up
                        open_card.append(deck_of_cards[0])  #add card to faceup pile, turn faceup and delete from deck
                        deck_of_cards.pop(0)
                        open_card[0].set_up_true()

                        print("Cards in deck")
                        for item in deck_of_cards:
                            print(item)

                        print("Card in hand")
                        print(open_card[0])

                    elif len(open_card) > 0:                    # if a card is already face up
                        open_card[0].set_down_true()            #set curr face up to face down, add to back of deck, pop from faceup list
                        deck_of_cards.append(open_card[0])      #add new card to faceup list
                       
                        open_card.pop(0)
                        open_card.append(deck_of_cards[0])
                        open_card[0].set_up_true()
                        deck_of_cards.pop(0)

                        print("Cards in deck")
                        for item in deck_of_cards:
                            print(item)

                        print("Card in hand")
                        print(open_card[0])


            if event.type == timer.get_timer_event():
                timer.reduce_counter(open_card, deck_of_cards)
            btn.get_event(event)

        
        draw(WIN, deck_of_cards, open_card, btn, timer)
        pygame.display.update()


    pygame.quit()

    
main()

    
    






