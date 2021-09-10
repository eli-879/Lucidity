import pygame

class Sound:
    def __init__(self, rect, **kwargs):
        #updating attributes depending on any additional things entered
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        
        self.sound_text = self.font.render(str(int(self.sound * 100)) + "%", True, (255, 255, 255))
        self.sound_rect = self.sound_text.get_rect(center = self.rect.center)
        self.title = self.font.render(self.text, True, (255, 255, 255))
        self.title_rect = self.sound_text.get_rect(left = self.rect.left + 10, top = self.rect.top)

    #can pass dictionary with many new settings into kwargs to change it
    def process_kwargs(self, kwargs):
        settings = {
            "color"               :pygame.Color("red"),
            "text"                :"Sound",
            "font"                :pygame.font.Font("Assets/Font/upheavtt.ttf", 36),
            "hover_color"         :(200,0,0),
            "font_color"          :pygame.Color("white"),
            "sound"               :0.5
            }

        #can pass dictionary with many new settings into kwargs to change it

        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))

        self.__dict__.update(settings)

    #increase and decrease sound
    def increase_sound(self):
        if self.sound < 1:
            self.sound += 0.1
            self.sound = round(self.sound, 1)

            self.sound_text = self.font.render(str(int(self.sound * 100)) + "%", True, (255,255,255))
            self.sound_rect = self.sound_text.get_rect(center = self.rect.center)

    def decrease_sound(self):
        if self.sound > 0:
            self.sound -= 0.1
            self.sound = round(self.sound, 1)
            self.sound_text = self.font.render(str(int(self.sound * 100)) + "%", True, (255,255,255))
            self.sound_rect = self.sound_text.get_rect(center = self.rect.center)

    def get_sound_level(self):
        return self.sound

    def draw(self, window):
        self.image.fill(self.color)
        window.blit(self.image,  self.rect)
        window.blit(self.sound_text, self.sound_rect)
        window.blit(self.title, self.title_rect)
