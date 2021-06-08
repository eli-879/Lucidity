import pygame

class Score:

    def __init__(self, rect, **kwargs):
        #updating attributes depending on any additional things entered
        self.process_kwargs(kwargs)
        self.__rect = pygame.Rect(rect)
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__score = 0
        self.__score_text = self.font.render(str(self.__score), True, (255, 255, 255))
        self.__score_rect = self.__score_text.get_rect(center = self.__rect.center)
        self.__title = self.font.render(self.text, True, (255, 255, 255))
        self.__title_rect = self.__score_text.get_rect(left = self.__rect.left + 10, top = self.__rect.top)

        self.__first_card = True

    #processing kwargs so that they are added as attributes if stated in initialization
    def process_kwargs(self, kwargs):
        settings = {
            "color"               :pygame.Color("red"),
            "text"                :"Score:",
            "font"                :pygame.font.Font("Assets/Font/upheavtt.ttf", 36),
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

    #checking and setting first card
    def is_first_card(self):
        return self.__first_card

    def set_first_card(self, value):
        self.__first_card = value
      
    #increase score 
    def increase_score(self):
        if self.__first_card == True:
            self.__first_card = False
            pass
        else:
            self.__score += 1
            self.__score_text = self.font.render(str(self.__score), True, (0,128,0))
            self.__score_rect = self.__score_text.get_rect(center = self.__rect.center)
           
    #reset score
    def reset_score(self):
        self.__first_card = True
        self.__score = 0
        self.__score_text = self.font.render(str(self.__score), True, (0,128,0))
        self.__score_rect = self.__score_text.get_rect(center = self.__rect.center)

    def draw(self, window):
        self.__image.fill(self.color)
        window.blit(self.__image,  self.__rect)
        window.blit(self.__score_text, self.__score_rect)
        window.blit(self.__title, self.__title_rect)
