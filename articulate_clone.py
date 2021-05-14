import pygame
import random
import json

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lucidity!")
FPS = 60
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
clock = pygame.time.Clock()
card_word_font = pygame.font.Font("upheavtt.ttf", 20)
main_menu_font = pygame.font.Font("upheavtt.ttf", 72)
peripherals_word_font = pygame.font.Font("upheavtt.ttf", 20)

BG = pygame.image.load("background.jpg")
CARD_BACK = pygame.image.load("card_back_v2.jpg")
CARD_FRONT = pygame.image.load("card_front.png")
START_BUTTON = pygame.image.load("play.png")
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
        self.__xpos_move = 0
        self.__ypos_fdown = (HEIGHT - (self.__HEIGHT) * 2) / 3
        self.__ypos_fup =  (2 * ((HEIGHT - (self.__HEIGHT) * 2) / 3)) + self.__HEIGHT
        self.__ypos_move = 0
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
            category_0 = card_word_font.render(self.__list_of_items[0], 1, BLACK)
            category_1 = card_word_font.render(self.__list_of_items[1], 1, BLACK)
            category_2 = card_word_font.render(self.__list_of_items[2], 1, BLACK)
            category_3 = card_word_font.render(self.__list_of_items[3], 1, BLACK)
            category_4 = card_word_font.render(self.__list_of_items[4], 1, BLACK)
            category_5 = card_word_font.render(self.__list_of_items[5], 1, BLACK)

            list_of_cat = [category_0, category_1, category_2, category_3, category_4, category_5]

            for i in range(len(list_of_cat)): # drawing open card
                initial_y_pos = self.__ypos_fup + 41 - list_of_cat[i].get_height()      
                y_gaps = 7.5 * i
                center_box = ((36 - list_of_cat[i].get_height()) / 2) + ((i) * 36)
                window.blit(list_of_cat[i], (self.__xpos + 60, initial_y_pos + center_box + y_gaps))

                if i == self.__ace_index:
                    window.blit(self.__ace, (self.__xpos + 370 - 17.4, initial_y_pos + center_box + y_gaps - 5))
       
        elif self.__down == True:
            window.blit(self.__card_back, (self.__xpos, self.__ypos_fdown))

    def draw_open_card(self, window, x_pos, y_pos):
        window.blit(self.__card_front, (x_pos, y_pos))
        category_0 = card_word_font.render(self.__list_of_items[0], 1, BLACK)
        category_1 = card_word_font.render(self.__list_of_items[1], 1, BLACK)
        category_2 = card_word_font.render(self.__list_of_items[2], 1, BLACK)
        category_3 = card_word_font.render(self.__list_of_items[3], 1, BLACK)
        category_4 = card_word_font.render(self.__list_of_items[4], 1, BLACK)
        category_5 = card_word_font.render(self.__list_of_items[5], 1, BLACK)

        list_of_cat = [category_0, category_1, category_2, category_3, category_4, category_5]

        for i in range(len(list_of_cat)): # drawing open card
            initial_y_pos = y_pos + 38 - list_of_cat[i].get_height()      
            y_gaps = 7.5 * i
            center_box = ((36 - list_of_cat[i].get_height()) / 2) + ((i) * 36)
            window.blit(list_of_cat[i], (x_pos + 60, initial_y_pos + center_box + y_gaps))

            if i == self.__ace_index:
                window.blit(self.__ace, (x_pos + 370 - 17.4, initial_y_pos + center_box + y_gaps - 5))



    def get_x_coords(self):
        return (self.__xpos, self.__xpos + self.__WIDTH)

    def get_y_coords_fup(self):
        return (self.__ypos_fup, self.__ypos_fup + self.__HEIGHT)

    def get_y_coords_fdown(self):
        return (self.__ypos_fdown, self.__ypos_fdown + self.__HEIGHT)


    def add_x_coords(self, value):
        self.__xpos += value

    def add_y_coords_fup(self, value):
        self.__ypos_fup += value

    def add_y_coords_fdown(self, value):
        self.__ypos_fdown += value


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
            "color"               :pygame.Color("black"),
            "text"                :"Start Round",
            "font"                :pygame.font.Font("upheavtt.ttf", 20),
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
        if self.is_hovering():
            self.__command()

    def is_hovering(self):
        
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, window):
        if self.is_hovering():
            self.__image.fill(self.hover_color)
        else:
            self.__image.fill(self.color)
            
        window.blit(self.__image, self.__rect)
        window.blit(self.text, self.text_rect)

class Timer:

    def __init__(self, rect, seconds, beep, **kwargs):
        self.process_kwargs( kwargs)
        self.__rect = pygame.Rect(rect)        
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__counter = seconds
        self.__counter_fixed = seconds

        self.__text = self.font.render(str(self.__counter), True, (255, 255, 255))
        self.__text_rect = self.__text.get_rect(center = self.__rect.center)
        self.__title = self.font.render("Timer:", True, (255, 255, 255))
        self.__title_rect = self.__text.get_rect(left = self.__rect.left + 10, top = self.__rect.top)

        self.__timer_event = pygame.USEREVENT + 1
        self.__timer = pygame.time.set_timer(self.__timer_event, 1000)
        self.__beep = beep

    def process_kwargs(self, kwargs):
        settings = {
            "color"               :pygame.Color("black"),
            "text"                :"Start Round",
            "font"                :pygame.font.Font("upheavtt.ttf", 36),
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

    def get_timer_event(self):
        return self.__timer_event

    def reduce_counter(self, open_card, deck_of_cards, score):
        self.__counter -= 1
        self.__text = self.font.render(str(self.__counter), True, (255,255,255))
        self.__text_rect = self.__text.get_rect(center = self.__rect.center)

        if self.__counter == 10:
            pygame.mixer.Sound.play(self.__beep)

        if self.__counter == 0:
            pygame.mixer.Sound.play(self.__beep, loops=2)
            score.reset_score()
            

        if self.__counter <= 0:
            self.__timer = pygame.time.set_timer(self.__timer_event, 0)
            if len(open_card) >= 1:
                open_card[0].set_down_true()              
                open_card.pop(0)
                
            else:
                pass

    def reset(self):
        self.__counter = self.__counter_fixed + 1
        self.__timer = pygame.time.set_timer(self.__timer_event, 1000)

    def draw(self, window):
        #self.__image.fill(self.color)
        window.blit(self.__image, self.__rect)
        window.blit(self.__text, self.__text_rect)
        window.blit(self.__title, self.__title_rect)

class Score:

    def __init__(self, rect, **kwargs):
        self.process_kwargs(kwargs)
        self.__rect = pygame.Rect(rect)
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__score = 0
        self.__text = self.font.render(str(self.__score), True, (255, 255, 255))
        self.__score_rect = self.__text.get_rect(center = self.__rect.center)
        self.__title = self.font.render("Score:", True, (255, 255, 255))
        self.__title_rect = self.__text.get_rect(left = self.__rect.left + 10, top = self.__rect.top)

        self.__first_card = True

    def process_kwargs(self, kwargs):
        settings = {
            "color"               :pygame.Color("red"),
            "text"                :"Start Round",
            "font"                :pygame.font.Font("upheavtt.ttf", 36),
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

    def is_first_card(self):
        return self.__first_card

    def set_first_card(self, value):
        self.__first_card = value
      
    def increase_score(self):

        if self.__first_card == True:
            self.__first_card = False
            pass
        else:
            self.__score += 1
            self.__text = self.font.render(str(self.__score), True, (0,128,0))
            self.__score_rect = self.__text.get_rect(center = self.__rect.center)        

    def reset_score(self):
        self.__first_card = True
        self.__score = 0
        self.__text = self.font.render(str(self.__score), True, (0,128,0))
        self.__score_rect = self.__text.get_rect(center = self.__rect.center)

    def draw(self, window):
        self.__image.fill(self.color)
        window.blit(self.__image,  self.__rect)
        window.blit(self.__text, self.__score_rect)
        window.blit(self.__title, self.__title_rect)


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
        
        for i in range(len(hand_list) -1, -1, -1):
            x_pos = hand_list[i].get_x_coords()[0]
            y_pos = hand_list[i].get_y_coords_fup()[0]
            hand_list[i].draw_open_card(window, x_pos + (i * 25), y_pos + (i * -25))

def draw(window, deck_of_cards, open_hand, start_button, timer, skip_button):
    WIN.blit(BG, (0,0))
    #WIN.fill(GREY)
    deck_of_cards[0].draw(WIN)
    draw_hand(WIN, open_hand)
    start_button.draw(WIN)
    timer.draw(WIN)
    skip_button.draw(WIN)

def start_button_press(timer, score, deck_of_cards, open_card):
    timer.reset()
    score.reset_score()
    deck_of_cards.extend(open_card)
    for i in range(len(open_card)):
        open_card.pop(0)

def skip_button_press(deck_of_cards, open_card):     
    if len(open_card) == 1:                                                    
        open_card.insert(0, deck_of_cards[0])
        deck_of_cards.pop(0)

        print(open_card)

    else:
        pass

def main_menu():
    run = True
    
    while run:
        
        WIN.blit(BG, (0,0))
        title_label = main_menu_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame. MOUSEBUTTONDOWN:
                main()


        
    pygame.quit()

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

    ambient_music = pygame.mixer.Sound("seashanty2.mp3")
    ambient_music.set_volume(0.1)
    pygame.mixer.Sound.play(ambient_music, loops=-1)

    beep = pygame.mixer.Sound("beep.wav")
    beep.set_volume(0.5)

    card_fdown_x = deck_of_cards[0].get_x_coords()
    card_fdown_y = deck_of_cards[0].get_y_coords_fdown()
    start_button_x = (card_fdown_x[0] - 200) / 2
    timer_x = (card_fdown_x[1] + ((1280 - card_fdown_x[1]) - 200) / 2)

    timer = Timer(rect=(timer_x, 176.66, 200, 100), seconds=30, beep = beep)
    score = Score(rect=(timer_x, card_fdown_y[0], 200, 100))
    start_button = Button(rect=(start_button_x, card_fdown_y[0], 200, 25), command = lambda timer=timer, score=score, deck_of_cards=deck_of_cards, open_card = open_card:start_button_press(timer, score, deck_of_cards, open_card))
    skip_button = Button(rect=(start_button_x, card_fdown_y[0] + 50, 200, 25), command = lambda deck_of_cards=deck_of_cards, open_card=open_card:skip_button_press(deck_of_cards, open_card), text="Skip Card")
    
    run = True


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():                    #check if exit is clicked
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):                    #check if mouse is pressed
                x_pos, y_pos = pygame.mouse.get_pos()
                print(x_pos, y_pos)
                
                
                if (deck_of_cards[0].get_x_coords()[0] <= x_pos <= deck_of_cards[0].get_x_coords()[1]) and \
                    (deck_of_cards[0].get_y_coords_fdown()[0] <= y_pos <= deck_of_cards[0].get_y_coords_fdown()[1]) \
                    or ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):                 #if mouse click loc is within card range, go to next card
                    

                    if len(open_card) == 0:                 #if no cards are face up
                        open_card.append(deck_of_cards[0])  #add card to faceup pile, turn faceup and delete from deck
                        deck_of_cards.pop(0)
                        open_card[0].set_up_true()
                        score.increase_score()

                    elif len(open_card) > 0:                    # if a card is already face up
                        open_card[0].set_down_true()            #set curr face up to face down, add to back of deck, pop from faceup list
                        deck_of_cards.append(open_card[0])      #add new card to faceup list
                       
                        open_card.pop(0)
                        open_card.insert(0, deck_of_cards[0])
                        open_card[0].set_up_true()
                        deck_of_cards.pop(0)
                        score.increase_score()
                    
                #if player clicks on open card, then switch the two available cards around
                if len(open_card) > 0:
                    if (open_card[0].get_x_coords()[0] <= x_pos <= open_card[0].get_x_coords()[1]) and \
                        (open_card[0].get_y_coords_fup()[0] <= y_pos <= open_card[0].get_y_coords_fup()[1]) and \
                        len(open_card) == 2:

                        temp = open_card[0]
                        open_card[0] = open_card[1]
                        open_card[1] = temp
           
                    print(open_card)

            if event.type == timer.get_timer_event():
                timer.reduce_counter(open_card, deck_of_cards, score)

            start_button.get_event(event)
            skip_button.get_event(event)

        
        draw(WIN, deck_of_cards, open_card, start_button, timer, skip_button)
        score.draw(WIN)
        pygame.display.update()


main_menu()

    
    






