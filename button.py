import pygame

class Button:

    def __init__(self, rect, command=None, **kwargs):
        #updating attributes depending on any additional things entered
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.command = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center = self.rect.center)

    #processing kwargs so that they are added as attributes if stated in initialization
    def process_kwargs(self, kwargs):
        settings = {
            "color"               :pygame.Color("black"),
            "text"                :"Start Round",
            "font"                :pygame.font.Font("Assets/Font/upheavtt.ttf", 20),
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

    #getting event
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.is_hovering():
            self.command()

    def is_clicked(self, event):
        if self.is_hovering() and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return True
        return False

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, window):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
            
        window.blit(self.image, self.rect)
        window.blit(self.text, self.text_rect)
