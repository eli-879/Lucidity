import pygame

class Timer:

    def __init__(self, rect, seconds, beep, **kwargs):
        self.process_kwargs( kwargs)
        self.__rect = pygame.Rect(rect)        
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__counter = seconds
        self.__counter_fixed = seconds
        self.__start = False

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

    def get_timer_event(self):
        return self.__timer_event

    def reduce_counter(self, open_card, deck_of_cards, score):
        if self.__start == True:

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

    def start_timer(self):
        self.__start = True


    def reset(self):
        self.__counter = self.__counter_fixed + 1
        self.__timer = pygame.time.set_timer(self.__timer_event, 1000)

    def draw(self, window):
        #self.__image.fill(self.color)
        window.blit(self.__image, self.__rect)
        window.blit(self.__text, self.__text_rect)
        window.blit(self.__title, self.__title_rect)
