import pygame
BLACK = (0,0,0)
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def reset(self):
       self.rect.y = 322.5
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
    #Check that you are not going too far (off the screen)
        if self.rect.y > 570:
          self.rect.y = 570