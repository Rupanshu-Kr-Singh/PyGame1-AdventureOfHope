import pygame
import random

class MovableObject:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.platform = pygame.Rect(x, y, width, 20)
    
    def update_platform(self):
        """Update platform position based on object position"""
        self.platform.x = self.x
        self.platform.y = self.y
    
    def draw(self, screen):
        """Draw the object"""
        screen.blit(self.image, (self.x, self.y))
    
    def get_platform(self):
        """Return the platform rect for collision"""
        return self.platform


class GlitterObject(MovableObject):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        self.alpha = 255
        self.glitter = True
    
    def draw(self, screen):
        """Draw the object with glitter effect"""
        if self.glitter:
            self.alpha = random.randint(150, 255)
        
        image_surface = self.image.copy()
        image_surface.set_alpha(self.alpha)
        screen.blit(image_surface, (self.x, self.y))