from re import L
import pygame
import os

#importing class from separate files
from button import Button
from timer import Timer
from score import Score
from sound import Sound
from animated_sprite import AnimatedSprite
from deck import Deck

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lucidity")
FPS = 60
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
clock = pygame.time.Clock()

#adding assets
card_word_font = pygame.font.Font("Assets/Font/upheavtt.ttf", 20)
main_menu_font = pygame.font.Font("Assets/Font/upheavtt.ttf", 72)
peripherals_word_font = pygame.font.Font("Assets/Font/upheavtt.ttf", 20)

BG = pygame.image.load("Assets/background.jpg")

START_BUTTON = pygame.image.load("Assets/play.png")

CARD_BACK = pygame.image.load("Assets/CardImages/card_back_v2.jpg")
CARD_FRONT = pygame.image.load("Assets/CardImages/card_front.png")

CARD_FRONT = pygame.transform.scale(CARD_FRONT, (400, 300))
CARD_BACK = pygame.transform.scale(CARD_BACK, (400, 300))

SPADES = pygame.image.load("Assets/CardImages/spades.png")
SPADES = pygame.transform.scale(SPADES, (30, 30))

CARD_ASSETS = [CARD_FRONT, CARD_BACK, SPADES, card_word_font, BLACK]

LOGO = pygame.image.load("Assets/logo.png")
LOGO = pygame.transform.scale(LOGO, (480, 171))

BOARD = pygame.image.load("Assets/board.png")

DATA = "TextFiles/data.txt"

#storing locations for each dino character
PLAYER_LOCS_FILE = "Assets/PlayerLocations.txt"
players = 3

#resetting location file each time game opened
with open(PLAYER_LOCS_FILE, "w") as file:
    for i in range(players):
        file.write("100 " + str(100 + i * 50) + "\n")


#Loading images for animated sprites
def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        image = pygame.transform.scale(image, (64, 64))
        images.append(image)

    return images

#Drawing Functions

def draw_main_menu(window, start_button, options_button, quit_button):
    start_button.draw(window)
    options_button.draw(window)
    quit_button.draw(window)

def draw_options_menu(window, sound_level, sound_quieter, sound_louder, back_button):
    sound_level.draw(WIN)
    sound_quieter.draw(WIN)
    sound_louder.draw(WIN)
    back_button.draw(WIN)

def draw_board(window, back_button):
    back_button.draw(window)

def draw_hand(window, hand_list):
    #drawing open hand cards - can't put in object as need to edit location per draw
    if len(hand_list) > 0:
        
        for i in range(len(hand_list) -1, -1, -1):
            x_pos = hand_list[i].get_x_coords()[0]
            y_pos = hand_list[i].get_y_coords_fup()[0]
            hand_list[i].draw_open_card(window, x_pos + (i * 25), y_pos + (i * -25))

def draw_game(window, deck_of_cards, open_hand, start_button, timer, skip_button, main_menu, board_button):
    WIN.blit(BG, (0,0))
    deck_of_cards[0].draw_fdown(WIN)
    draw_hand(WIN, open_hand)
    start_button.draw(WIN)
    timer.draw(WIN)
    skip_button.draw(WIN)
    main_menu.draw(WIN)
    board_button.draw(WIN)

#Button Functions

def start_button_press(timer, score, deck_of_cards, open_card):
    timer.start_timer()
    timer.reset()
    score.reset_score()
    deck_of_cards.extend(open_card)
    for i in range(len(open_card)):
        open_card.pop(0)

def skip_button_press(deck_of_cards, open_card):     
    if len(open_card) == 1:                                                    
        open_card.insert(0, deck_of_cards[0])
        deck_of_cards.pop(0)

#buttons at main menu
def play():
    pass

def quit():
    pygame.quit()

def options():
    options_menu()

class MainMenu: 
    def __init__(self, window, sound_level):
        self.window = window
        self.sound_level = sound_level
        self.button_width = 360
        self.button_height = 100
        self.button_x = (WIDTH - self.button_width) / 2
        self.button_y = (WIDTH - self.button_height) / 3
        
        self.start_button = Button(rect=(self.button_x, self.button_y, self.button_width, self.button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48), text="Play")
        self.options_button = Button(rect=(self.button_x, self.button_y+110, self.button_width, self.button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48), text="Options")
        self.quit_button = Button(rect=(self.button_x, self.button_y+220, self.button_width, self.button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48),text="Quit")

        self.buttons = [self.start_button, self.options_button, self.quit_button]

        self.logo_rect = pygame.Surface(LOGO.get_size())
        self.logo_size = LOGO.get_size()
        self.logo_x = (WIDTH - self.logo_size[0]) / 2

        self.ambient_music = pygame.mixer.Sound("Assets/Sounds/clanliness.ogg")
        self.ambient_music.set_volume(self.sound_level)
        pygame.mixer.Sound.play(self.ambient_music, loops=-1)

        self.quit = False

    
    def updateButtons(self, event):
        for button in self.buttons:
            if (button.is_clicked(event)):
                if (button == self.start_button):
                    game.getStates().append(MainGame(game.getWindow(), game.getDeck()))
                elif (button == self.options_button):
                    game.getStates().append(OptionsMenu(game.getWindow()))
                elif (button == self.quit_button):
                    pygame.quit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            self.updateButtons(event)
            

    def draw(self):
        self.window.blit(BG, (0,0))
        self.window.blit(LOGO, (self.logo_x, 20))

        self.start_button.draw(self.window)
        self.options_button.draw(self.window)
        self.quit_button.draw(self.window)

    def get_quit(self):
        return self.quit

class OptionsMenu:
    def __init__(self, window):
        self.window = window
        self.button_width = 200
        self.button_height = 70
        self.button_x = (WIDTH - self.button_width) / 2
        self.button_y = (WIDTH - self.button_height) / 3

        #initializing options menu buttons
        self.sound_level = Sound(rect=( self.button_x,  self.button_y, 200, self. button_height), text="Sound")
        self.sound_quieter_button = Button(rect=( self.button_x - 90 ,  self.button_y,  self.button_height,  self.button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48), text="-", command=lambda sound_level= self.sound_level:self.decrease_vol(sound_level))
        self.sound_louder_button = Button(rect=( self.button_x + 220,  self.button_y,  self.button_height,  self.button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48),text="+", command=lambda sound_level= self.sound_level:self.increase_vol(sound_level))
        self.back_button = Button(rect=( self.button_x,  self.button_y + 300, 200, 25), text="Back to Main Menu", command = lambda sound_level= self.sound_level:main_menu(self.sound_level.get_sound_level()))

        self.quit = False

    #functions if volume changed
    def increase_vol(self, sound_level):
        self.sound_level.increase_sound()

    def decrease_vol(self, sound_level):
        self.sound_level.decrease_sound()
    
    def get_quit(self):
        return self.quit

    def draw(self):
        pass

    def update(self):
        pass

class BoardMenu:
    def __init__(self, window, board, player_locs_file):
        self.board = board
        self.player_locs = []
        self.player_locs_file = player_locs_file
        self.window = window
    
        #initializing sprites images
        self.player_list = []
        self.images_list = []
        self.images_red = load_images(path="Assets/DinoRed")
        self.images_blue = load_images(path="Assets/DinoBlue")
        self.images_green = load_images(path="Assets/DinoGreen")
        
        self.images_list.append(self.images_red)
        self.images_list.append(self.images_blue)
        self.images_list.append(self.images_green)
        
        self.num_players = 3

        self.all_sprites = pygame.sprite.Group()

        self.back_button = Button(rect=(50, 50, 200, 40), text="Back to Game", command = lambda player_locs_file=player_locs_file, num_players = self.num_players : self.back_button_funcs(self.player_locs_file, self.num_players))

        self.draw_list = []

        self.quit = False
        self.offset_x = 0
        self.offset_y = 0

        self.init_player_locs()

        #initializing sprite objects
        for i in range(self.num_players):
            data = self.player_locs[i]
            location = (int(data[0]), int(data[1]))
            images = self.images_list[i]
            new_player = AnimatedSprite(position=location, images=images)
            self.player_list.append(new_player)
            self.all_sprites.add(new_player)

    
    def init_player_locs(self):
        with open(self.player_locs_file, "r") as file:
            file_lines = file.readlines()
            for line in file_lines:
                data = line.split()
                self.player_locs.append(data)

    def write_loc_to_file(self, player_locs_file, num_players):
        with open(player_locs_file, "w") as file:
            for i in range(num_players):
                player_loc = self.player_list[i].get_rect()
                player_loc_str = str(player_loc[0]) + " " + str(player_loc[1])
                file.write(player_loc_str + "\n")
    
    #function for doing writing locations to file when back button pressed and changing screen back to main game
    def back_button_funcs(self, num_players):
        self.write_loc_to_file(self.player_locs_file, num_players)

    def updateButtons(self, event):
        if (self.back_button.is_clicked(event)):
            self.back_button_funcs(self.num_players)
            game.getStates().pop()

    def updateDinos(self, event):
        #handles what happens if a sprite is clicked - makes sure only one sprite can be moved at a time
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for player in self.player_list[::-1]:
                        if player.get_rect().collidepoint(event.pos):
                            self.draw_list.append(player)
                            self.draw_list[0].set_dragging(True)
                            mouse_x, mouse_y = event.pos
                            self.offset_x = self.draw_list[0].get_rect().x - mouse_x
                            self.offset_y = self.draw_list[0].get_rect().y - mouse_y
            
            #if clicked off let sprite go
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if len(self.draw_list) > 0:
                        self.draw_list[0].set_position((self.draw_list[0].get_rect().x, self.draw_list[0].get_rect().y))

                    for player in self.player_list:
                        player.set_dragging(False)                    
                   
                    self.draw_list.clear()
            
            #change sprite location as mouse moves
            elif event.type == pygame.MOUSEMOTION:
                for player in self.player_list:
                    if player.get_dragging() == True:
                        mouse_x, mouse_y = event.pos
                        player.get_rect().x = mouse_x + self.offset_x
                        player.get_rect().y = mouse_y + self.offset_y

    def update(self):
        dt = clock.tick(FPS) / 1000 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            self.updateButtons(event)
            self.updateDinos(event)
        self.all_sprites.update(dt)

        

    def draw(self):
        self.window.blit(self.board, (0,0))
        self.back_button.draw(self.window)
        self.all_sprites.draw(self.window)

    def get_quit(self):
        return self.quit

class MainGame:
    def __init__(self, window, deck):
        self.window = window
        self.deck_of_cards = deck
        self.open_card = []
        self.beep = pygame.mixer.Sound("Assets/Sounds/beep.wav")
        self.beep.set_volume(0.5)

        self.card_fdown_x = self.deck_of_cards[0].get_x_coords()
        self.card_fdown_y = self.deck_of_cards[0].get_y_coords_fdown()
        self.start_button_x = (self.card_fdown_x[0] - 200) / 2
        self.timer_x = (self.card_fdown_x[1] + ((1280 - self.card_fdown_x[1]) - 200) / 2)

        #initializing buttons
        self.timer = Timer(rect=(self.timer_x, 176.66, 200, 100), seconds=30, beep = self.beep)
        self.score = Score(rect=(self.timer_x, self.card_fdown_y[0], 200, 100))
        self.start_button = Button(rect=(self.start_button_x, self.card_fdown_y[0], 200, 40))
        self.skip_button = Button(rect=(self.start_button_x, self.card_fdown_y[0] + 60, 200, 40), text="Skip Card")
        self.board_button = Button(rect=(self.start_button_x, self.card_fdown_y[0] + 120, 200, 40), text="View Board")
        self.back_button = Button(rect=(self.start_button_x, self.card_fdown_y[0] + 500, 200, 40), text="Back to Main Menu")

        self.buttons = [self.start_button, self.skip_button, self.board_button, self.back_button]

        self.quit = False

    def start_button_press(self):
        self.timer.start_timer()
        self.timer.reset()
        self.score.reset_score()
        game.getDeck().extend(self.open_card)
        for i in range(len(self.open_card)):
            self.open_card.pop(0)

    def skip_button_press(self):     
        if len(self.open_card) == 1:                                                    
            self.open_card.insert(0, game.getDeck()[0])
            game.getDeck().pop(0)


    def draw_hand(self, window, hand_list):
        #drawing open hand cards - can't put in object as need to edit location per draw
        if len(hand_list) > 0:
            for i in range(len(hand_list) -1, -1, -1):
                x_pos = hand_list[i].get_x_coords()[0]
                y_pos = hand_list[i].get_y_coords_fup()[0]
                hand_list[i].draw_open_card(window, x_pos + (i * 25), y_pos + (i * -25))
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            self.updateButtons(event)
            self.updateCard(event)
            self.updateTimer(event)
             
    def updateButtons(self, event):
        for button in self.buttons:
            if (button.is_clicked(event)):
                if (button == self.start_button):
                    self.start_button_press()
                elif (button == self.skip_button):
                    self.skip_button_press()
                elif (button == self.board_button):
                    game.getStates().append(BoardMenu(game.getWindow(), game.getBoard(), game.getPlayerLocFiles()))
                elif (button == self.back_button):
                    game.getStates().pop()

    def updateCard(self, event):
        #check if mouse is pressed or space pressed
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):                    
                x_pos, y_pos = pygame.mouse.get_pos()                
                
                #if mouse click loc is within card range or space pressed, go to next card
                if (game.getDeck()[0].get_x_coords()[0] <= x_pos <= game.getDeck()[0].get_x_coords()[1]) and \
                    (game.getDeck()[0].get_y_coords_fdown()[0] <= y_pos <= game.getDeck()[0].get_y_coords_fdown()[1]) \
                    or ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):                 
                    
                    #if no cards are face up add card to faceup pile, turn faceup and delete from deck
                    if len(self.open_card) == 0:                 
                        self.open_card.append(game.getDeck()[0])  
                        game.getDeck().pop(0)
                        self.open_card[0].set_up_true()
                        self.score.increase_score()

                    # if a card is already face up set curr face up to face down, add to back of deck, pop from faceup list add new card to faceup list
                    elif len(self.open_card) > 0:                    
                        self.open_card[0].set_down_true()            
                        game.getDeck().append(self.open_card[0])      
                       
                        self.open_card.pop(0)
                        self.open_card.insert(0, game.getDeck()[0])
                        self.open_card[0].set_up_true()
                        game.getDeck().pop(0)
                        self.score.increase_score()
                    
                #if player clicks on open card, then switch the two available cards around
                if len(self.open_card) > 0:
                    if (self.open_card[0].get_x_coords()[0] <= x_pos <= self.open_card[0].get_x_coords()[1]) and \
                        (self.open_card[0].get_y_coords_fup()[0] <= y_pos <= self.open_card[0].get_y_coords_fup()[1]) and \
                        len(self.open_card) == 2:

                        temp = self.open_card[0]
                        self.open_card[0] = self.open_card[1]
                        self.open_card[1] = temp
        
    def updateTimer(self, event):
        #handling timer
        if event.type == self.timer.get_timer_event():
            self.timer.reduce_counter(self.open_card, game.getDeck(), self.score)

    def draw(self):
        
        self.deck_of_cards[0].draw_fdown(self.window)
        self.draw_hand(self.window, self.open_card)
        self.start_button.draw(self.window)
        self.timer.draw(self.window)
        self.skip_button.draw(self.window)
        self.back_button.draw(self.window)
        self.board_button.draw(self.window)
        self.score.draw(self.window)

    def get_quit(self):
        return self.quit


def main_menu(sound_level = 0.3):
    pygame.mixer.stop()
    run = True

    button_width = 360
    button_height = 100

    button_x = (WIDTH - button_width) / 2
    button_y = (HEIGHT - button_height) / 3

    #initializing buttons
    start_button = Button(rect=(button_x, button_y, button_width, button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48), text="Play", command=play)
    options_button = Button(rect=(button_x, button_y+110, button_width, button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48), text="Options", command=options)
    quit_button = Button(rect=(button_x, button_y+220, button_width, button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48),text="Quit", command = quit)

    #creating logo surface
    logo_rect = pygame.Surface(LOGO.get_size())
    logo_size = LOGO.get_size()
    logo_x = (WIDTH - logo_size[0]) / 2

    #loading in music
    ambient_music = pygame.mixer.Sound("Assets/Sounds/clanliness.ogg")
    ambient_music.set_volume(sound_level)
    pygame.mixer.Sound.play(ambient_music, loops=-1)
    
    #main loop
    while run:
        
        WIN.blit(BG, (0,0))
        WIN.blit(LOGO, (logo_x, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main_game(deck_of_cards)

            start_button.get_event(event)
            options_button.get_event(event)
            quit_button.get_event(event)

        draw_main_menu(WIN, start_button, options_button, quit_button)

        pygame.display.update()
        
    pygame.quit()

def options_menu(sound_level=0.3):

    #functions if volume changed
    def increase_vol(sound_level):
        sound_level.increase_sound()

    def decrease_vol(sound_level):
        sound_level.decrease_sound()

    run = True

    button_width = 200
    button_height = 70

    button_x = (WIDTH - button_width) / 2
    button_y = (HEIGHT - button_height) / 3

    #initializing options menu buttons
    sound_level = Sound(rect=(button_x, button_y, 200, button_height), text="Sound")
    sound_quieter_button = Button(rect=(button_x - 90 , button_y, button_height, button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48), text="-", command=lambda sound_level=sound_level:decrease_vol(sound_level))
    sound_louder_button = Button(rect=(button_x + 220, button_y, button_height, button_height), font=pygame.font.Font("Assets/Font/upheavtt.ttf", 48),text="+", command=lambda sound_level=sound_level:increase_vol(sound_level))
    back_button = Button(rect=(button_x, button_y + 300, 200, 25), text="Back to Main Menu", command = lambda sound_level=sound_level:main_menu(sound_level.get_sound_level()))

    while run:
        WIN.blit(BG, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            sound_quieter_button.get_event(event)
            sound_louder_button.get_event(event)
            back_button.get_event(event)

        draw_options_menu(WIN, sound_level, sound_quieter_button, sound_louder_button, back_button)
            
        pygame.display.update()

    pygame.quit()

def board_menu(player_locs_file):
    #function for writing location to location file when switched off of board screen
   

    #reading in player locations from file into list
    player_locs = []
    with open(player_locs_file, "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            data = line.split()
            player_locs.append(data)
    
    #initializing sprites images
    player_list = []
    images_list = []
    images_red = load_images(path="Assets/DinoRed")
    images_blue = load_images(path="Assets/DinoBlue")
    images_green = load_images(path="Assets/DinoGreen")
    
    images_list.append(images_red)
    images_list.append(images_blue)
    images_list.append(images_green)
    
    num_players = 3

    all_sprites = pygame.sprite.Group()

    #initializing sprite objects
    for i in range(num_players):
        data = player_locs[i]
        location = (int(data[0]), int(data[1]))
        images = images_list[i]
        new_player = AnimatedSprite(position=location, images=images)
        player_list.append(new_player)
        all_sprites.add(new_player)

    run = True

    back_button = Button(rect=(50, 50, 200, 40), text="Back to Game", command = lambda player_locs_file=player_locs_file, num_players = num_players : back_button_funcs(player_locs_file, num_players))

    draw_list = []

    while run:        

        WIN.blit(BG, (0,0))
        WIN.blit(BOARD, (0,0))

        #seconds between each loop
        dt = clock.tick(FPS) / 1000 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #handles what happens if a sprite is clicked - makes sure only one sprite can be moved at a time
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for player in player_list[::-1]:
                        if player.get_rect().collidepoint(event.pos):
                            draw_list.append(player)
                            draw_list[0].set_dragging(True)
                            mouse_x, mouse_y = event.pos
                            offset_x = draw_list[0].get_rect().x - mouse_x
                            offset_y = draw_list[0].get_rect().y - mouse_y
            
            #if clicked off let sprite go
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if len(draw_list) > 0:
                        draw_list[0].set_position((draw_list[0].get_rect().x, draw_list[0].get_rect().y))

                    for player in player_list:
                        player.set_dragging(False)                    
                   
                    draw_list.clear()
            
            #change sprite location as mouse moves
            elif event.type == pygame.MOUSEMOTION:
                for player in player_list:
                    if player.get_dragging() == True:
                        mouse_x, mouse_y = event.pos
                        player.get_rect().x = mouse_x + offset_x
                        player.get_rect().y = mouse_y + offset_y
            
            back_button.get_event(event)

        all_sprites.update(dt)

        all_sprites.draw(WIN)

        draw_board(WIN, back_button)

        pygame.display.update()
        
    pygame.quit()
    

def main_game(deck_of_cards):
    #main game screen
    open_card = []
    beep = pygame.mixer.Sound("Assets/Sounds/beep.wav")
    beep.set_volume(0.5)

    card_fdown_x = deck_of_cards[0].get_x_coords()
    card_fdown_y = deck_of_cards[0].get_y_coords_fdown()
    start_button_x = (card_fdown_x[0] - 200) / 2
    timer_x = (card_fdown_x[1] + ((1280 - card_fdown_x[1]) - 200) / 2)

    #initializing buttons
    timer = Timer(rect=(timer_x, 176.66, 200, 100), seconds=30, beep = beep)
    score = Score(rect=(timer_x, card_fdown_y[0], 200, 100))
    start_button = Button(rect=(start_button_x, card_fdown_y[0], 200, 40), command = lambda timer=timer, score=score, deck_of_cards=deck_of_cards, open_card = open_card:start_button_press(timer, score, deck_of_cards, open_card))
    skip_button = Button(rect=(start_button_x, card_fdown_y[0] + 60, 200, 40), text="Skip Card", command = lambda deck_of_cards=deck_of_cards, open_card=open_card:skip_button_press(deck_of_cards, open_card))
    board_button = Button(rect=(start_button_x, card_fdown_y[0] + 120, 200, 40), text="View Board", command = lambda player_locs_file = PLAYER_LOCS_FILE : board_menu(player_locs_file))
    back_button = Button(rect=(start_button_x, card_fdown_y[0] + 500, 200, 40), text="Back to Main Menu", command = main_menu)
    
    run = True

    while run:
        clock.tick(FPS)

        #check if exit is clicked
        for event in pygame.event.get():                   
            if event.type == pygame.QUIT:
                quit()

            #check if mouse is pressed or space pressed
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):                    
                x_pos, y_pos = pygame.mouse.get_pos()                
                
                #if mouse click loc is within card range or space pressed, go to next card
                if (deck_of_cards[0].get_x_coords()[0] <= x_pos <= deck_of_cards[0].get_x_coords()[1]) and \
                    (deck_of_cards[0].get_y_coords_fdown()[0] <= y_pos <= deck_of_cards[0].get_y_coords_fdown()[1]) \
                    or ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):                 
                    
                    #if no cards are face up add card to faceup pile, turn faceup and delete from deck
                    if len(open_card) == 0:                 
                        open_card.append(deck_of_cards[0])  
                        deck_of_cards.pop(0)
                        open_card[0].set_up_true()
                        score.increase_score()

                    # if a card is already face up set curr face up to face down, add to back of deck, pop from faceup list add new card to faceup list
                    elif len(open_card) > 0:                    
                        open_card[0].set_down_true()            
                        deck_of_cards.append(open_card[0])      
                       
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
            
            #handling timer
            if event.type == timer.get_timer_event():
                timer.reduce_counter(open_card, deck_of_cards, score)

            start_button.get_event(event)
            skip_button.get_event(event)
            back_button.get_event(event)
            board_button.get_event(event)
   
        draw_game(WIN, deck_of_cards, open_card, start_button, timer, skip_button, back_button, board_button)
        score.draw(WIN)
        pygame.display.update()


class Game:
    def __init__(self):
        self.states = []
        self.WIDTH, self.HEIGHT = 1280, 720
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Lucidity")
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.GREY = (150, 150, 150)
        self.clock = pygame.time.Clock()

        #adding assets
        self.card_word_font = pygame.font.Font("Assets/Font/upheavtt.ttf", 20)
        self.main_menu_font = pygame.font.Font("Assets/Font/upheavtt.ttf", 72)
        self.peripherals_word_font = pygame.font.Font("Assets/Font/upheavtt.ttf", 20)

        self.BG = pygame.image.load("Assets/background.jpg")

        self.START_BUTTON = pygame.image.load("Assets/play.png")

        self.CARD_BACK = pygame.image.load("Assets/CardImages/card_back_v2.jpg")
        self.CARD_FRONT = pygame.image.load("Assets/CardImages/card_front.png")

        self.CARD_FRONT = pygame.transform.scale(self.CARD_FRONT, (400, 300))
        self.CARD_BACK = pygame.transform.scale(self.CARD_BACK, (400, 300))

        self.SPADES = pygame.image.load("Assets/CardImages/spades.png")
        self.SPADES = pygame.transform.scale(self.SPADES, (30, 30))

        self.CARD_ASSETS = [self.CARD_FRONT, self.CARD_BACK,self. SPADES, self.card_word_font, self.BLACK]

        self.LOGO = pygame.image.load("Assets/logo.png")
        self.LOGO = pygame.transform.scale(self.LOGO, (480, 171))

        self.BOARD = pygame.image.load("Assets/board.png")

        self.DATA = "TextFiles/data.txt"

        #storing locations for each dino character
        self.PLAYER_LOCS_FILE = "Assets/PlayerLocations.txt"
        self.players = 3

        self.deck = Deck(self.DATA, self.WIDTH, self.HEIGHT, self.CARD_ASSETS)
        self.deck_of_cards = self.deck.generate_deck()

        #resetting location file each time game opened
        with open(self.PLAYER_LOCS_FILE, "w") as file:
            for i in range(self.players):
                file.write("100 " + str(100 + i * 50) + "\n")

    def initStates(self):
        self.states.append(MainMenu(self.WIN, 0.3))

    def getStates(self):
        return self.states

    def getWindow(self):
        return self.WIN

    def getDeck(self):
        return self.deck_of_cards

    def getPlayerLocFiles(self):
        return self.PLAYER_LOCS_FILE

    def getBoard(self):
        return self.BOARD

    def update(self):
        if (len(self.states) > 0):
            top = self.states[-1]

            top.update()

            if (top.get_quit()):
                pygame.quit()
        
        else:
            pygame.quit()
        
    def draw(self):
        self.WIN.blit(self.BG, (0,0))

        if (len(self.states) > 0):
            top = self.states[-1]

            top.draw()

        pygame.display.update()  

    def run(self):
        while True:
            self.update()
            self.draw()

#create deck of cards when program starts and starts at main menu
game = Game()
game.initStates()
game.run()

pygame.quit
