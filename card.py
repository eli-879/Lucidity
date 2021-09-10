class Card:
    
    def __init__(self, list_of_items, ace_index, screen_width, screen_height, card_assets):    
        self.up = False
        self.down = True
        self.HEIGHT = 300
        self.WIDTH = 400

        self.xpos = (screen_width - self.WIDTH) / 2
        self.xpos_move = 0
        self.ypos_fdown = (screen_height - (self.HEIGHT) * 2) / 3
        self.ypos_fup =  (2 * ((screen_height - (self.HEIGHT) * 2) / 3)) + self.HEIGHT
        self.ypos_move = 0
        
        self.card_front = card_assets[0]
        self.card_back = card_assets[1]
        self.ace = card_assets[2]
        self.font = card_assets[3]
        self.font_color = card_assets[4]

        self.mask = self.card_back.get_rect()
        self.people_item = list_of_items[0]
        self.world_item = list_of_items[1]
        self.object_item = list_of_items[2]
        self.action_item = list_of_items[3]
        self.nature_item = list_of_items[4]
        self.random_item = list_of_items[5]
        self.ace_index = ace_index[0]
        self.list_of_items = [self.people_item, self.world_item, self.object_item, self.action_item, self.nature_item, self.random_item]
 
    def __str__(self):
        string = str(self.list_of_items) + " Ace Category: " + str(self.ace_index)
        return string

    def draw_fdown(self, window):
        #draws facedown deck to the screen
        if self.down == True:
            window.blit(self.card_back, (self.xpos, self.ypos_fdown))

    def draw_open_card(self, window, x_pos, y_pos):
        #draws card in hand to screen
        window.blit(self.card_front, (x_pos, y_pos))
        category_0 = self.font.render(self.list_of_items[0], 1, self.font_color)
        category_1 = self.font.render(self.list_of_items[1], 1, self.font_color)
        category_2 = self.font.render(self.list_of_items[2], 1, self.font_color)
        category_3 = self.font.render(self.list_of_items[3], 1, self.font_color)
        category_4 = self.font.render(self.list_of_items[4], 1, self.font_color)
        category_5 = self.font.render(self.list_of_items[5], 1, self.font_color)

        list_of_cat = [category_0, category_1, category_2, category_3, category_4, category_5]

        # drawing open card items
        for i in range(len(list_of_cat)): 
            initial_y_pos = y_pos + 38 - list_of_cat[i].get_height()      
            y_gaps = 7.5 * i
            center_box = ((36 - list_of_cat[i].get_height()) / 2) + ((i) * 36)
            window.blit(list_of_cat[i], (x_pos + 60, initial_y_pos + center_box + y_gaps))

            if i == self.ace_index:
                window.blit(self.ace, (x_pos + 370 - 17.4, initial_y_pos + center_box + y_gaps - 5))

    def get_x_coords(self):
        return (self.xpos, self.xpos + self.WIDTH)

    def get_y_coords_fup(self):
        return (self.ypos_fup, self.ypos_fup + self.HEIGHT)

    def get_y_coords_fdown(self):
        return (self.ypos_fdown, self.ypos_fdown + self.HEIGHT)

    def add_x_coords(self, value):
        self.xpos += value

    def add_y_coords_fup(self, value):
        self.ypos_fup += value

    def add_y_coords_fdown(self, value):
        self.ypos_fdown += value

    def set_up_true(self):
        self.up = True
        self.down = False

    def set_down_true(self):
        self.up = False
        self.down = True
