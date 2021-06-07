import sound

class Sound:
    def __init__(self, rect, **kwargs):
        self.process_kwargs(kwargs)
        self.__rect = pygame.Rect(rect)
        self.__image = pygame.Surface(self.__rect.size).convert()
        self.__sound = 0.5
        self.__sound_text = self.font.render(str(int(self.__sound * 100)) + "%", True, (255, 255, 255))
        self.__sound_rect = self.__sound_text.get_rect(center = self.__rect.center)
        self.__title = self.font.render(self.text, True, (255, 255, 255))
        self.__title_rect = self.__sound_text.get_rect(left = self.__rect.left + 10, top = self.__rect.top)

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

    def increase_sound(self):
        if self.__sound < 1:
            self.__sound += 0.1
            self.__sound = round(self.__sound, 1)

            self.__sound_text = self.font.render(str(int(self.__sound * 100)) + "%", True, (255,255,255))
            self.__sound_rect = self.__sound_text.get_rect(center = self.__rect.center)
            print(self.__sound)

    def decrease_sound(self):
        if self.__sound > 0:
            self.__sound -= 0.1
            self.__sound = round(self.__sound, 1)
            self.__sound_text = self.font.render(str(int(self.__sound * 100)) + "%", True, (255,255,255))
            self.__sound_rect = self.__sound_text.get_rect(center = self.__rect.center)

    def get_sound_level(self):
        return self.__sound

    def draw(self, window):
        self.__image.fill(self.color)
        window.blit(self.__image,  self.__rect)
        window.blit(self.__sound_text, self.__sound_rect)
        window.blit(self.__title, self.__title_rect)
