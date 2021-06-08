import pygame

#inheriting from sprite class
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super().__init__()

        self.size = (64, 64)
        self.position = position
        self.rect = pygame.Rect(position, self.size)
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.dragging = False

        self.animation_frames = 6
        self.current_frame = 0

        self.current_time = 0
        self.animation_time = 0.1

    #updating animation depending on how many frames have passed
    def update_frame_dependent(self):
        self.current_frame += 1

        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
    
    #updating animation depending on how many bits of time have passed
    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index+1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)

    def get_rect(self):
        return self.rect

    def set_dragging(self, value):
        self.dragging = value

    def get_dragging(self):
        return self.dragging

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
  

