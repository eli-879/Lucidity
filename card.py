import pygame
pygame.init()

WIDTH, HEIGHT = 1280, 720




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
