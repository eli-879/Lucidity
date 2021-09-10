import pygame

class Score:

    def __init__(self, rect, **kwargs):
        #updating attributes depending on any additional things entered
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.score = 0
        self.score_text = self.font.render(str(self.score), True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect(center = self.rect.center)
        self.title = self.font.render(self.text, True, (255, 255, 255))
        self.title_rect = self.score_text.get_rect(left = self.rect.left + 10, top = self.rect.top)

        self.first_card = True

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
        return self.first_card

    def set_first_card(self, value):
        self.first_card = value
      
    #increase score 
    def increase_score(self):
        if self.first_card == True:
            self.first_card = False
            pass
        else:
            self.score += 1
            self.score_text = self.font.render(str(self.score), True, (0,128,0))
            self.score_rect = self.score_text.get_rect(center = self.rect.center)
           
    #reset score
    def reset_score(self):
        self.first_card = True
        self.score = 0
        self.score_text = self.font.render(str(self.score), True, (0,128,0))
        self.score_rect = self.score_text.get_rect(center = self.rect.center)

    def draw(self, window):
        self.image.fill(self.color)
        window.blit(self.image,  self.rect)
        window.blit(self.score_text, self.score_rect)
        window.blit(self.title, self.title_rect)
