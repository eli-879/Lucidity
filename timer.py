import pygame

class Timer:

    def __init__(self, rect, seconds, beep, **kwargs):
        #updating attributes depending on any additional things entered
        self.process_kwargs( kwargs)
        self.rect = pygame.Rect(rect)        
        self.image = pygame.Surface(self.rect.size).convert()
        self.counter = seconds
        self.counter_fixed = seconds
        self.start = False

        self.text = self.font.render(str(self.counter), True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center = self.rect.center)
        self.title = self.font.render("Timer:", True, (255, 255, 255))
        self.title_rect = self.text.get_rect(left = self.rect.left + 10, top = self.rect.top)

        self.timer_event = pygame.USEREVENT + 1
        self.timer = pygame.time.set_timer(self.timer_event, 1000)
        self.beep = beep

    #can pass dictionary with many new settings into kwargs to change it
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
        return self.timer_event

    #reduce timer by 1second every second
    def reduce_counter(self, open_card, deck_of_cards, score):
        if self.start == True:

            self.counter -= 1
            self.text = self.font.render(str(self.counter), True, (255,255,255))
            self.text_rect = self.text.get_rect(center = self.rect.center)

            if self.counter == 10:
                pygame.mixer.Sound.play(self.beep)

            if self.counter == 0:
                pygame.mixer.Sound.play(self.beep, loops=2)
                score.reset_score()
            
            if self.counter <= 0:
                self.timer = pygame.time.set_timer(self.timer_event, 0)
                if len(open_card) >= 1:
                    open_card[0].set_down_true()              
                    open_card.pop(0)        
                else:
                    pass

    def start_timer(self):
        self.start = True

    def reset(self):
        self.counter = self.counter_fixed + 1
        self.timer = pygame.time.set_timer(self.timer_event, 1000)

    def draw(self, window):
        window.blit(self.image, self.rect)
        window.blit(self.text, self.text_rect)
        window.blit(self.title, self.title_rect)
