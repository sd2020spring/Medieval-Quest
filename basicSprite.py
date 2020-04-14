import pygame
from helpers import *

class singleSprite(pygame.sprite.Sprite):
    """
    This class will be the initializer for the basic value of any sprite
    This means this class will initialize images and center points for all sprites
    """

    def __init__(self, centerPoint, image):
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.image = image
        self.rect = image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint


class multipleSprite(pygame.sprite.Sprite):
    """
    This class will be the initializer for the basic value of any sprite
    This means this class will initialize images and center points for all sprites
    """

    def __init__(self, centerPoint, images):
        pygame.sprite.Sprite.__init__(self)
        """Set the image and the rect"""
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint

class Heart(multipleSprite):
    """
    This is the class that will make sure that heart appear in the inventory
    """
    def __init__(self, centerPoint, images):
        multipleSprite.__init__(self, centerPoint, images)

    def update(self, level):
        if level == 3:
            self.image = self.images[0]
        elif level == 2:
            self.image = self.images[1]
        elif level == 1:
            self.image = self.images[2]

class BombInventory(singleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images):
        singleSprite.__init__(self, centerPoint, images)
        self.timer = 5
        self.gone = False

    def update(self, ground_image):
        self.timer -= 1
        if self.timer == 0:
            self.gone(ground_image)
            return True

    def gone(self, ground_image):
        self.gone = True
        self.images = ground_image

class Potion(singleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images):
        singleSprite.__init__(self, centerPoint, images)
        self.timer = 5
        self.gone = False

    def gone(self, ground_image):
        self.gone = True
        self.images = ground_image

class Numbers(multipleSprite):
    """
    This is the class that will make sure that numbers appear in the inventory
    """
    def __init__(self, centerPoint, images, number):
        multipleSprite.__init__(self, centerPoint, images)
        self.current = number

    def update(self, number):
        self.current = number
        self.image = self.images[self.current]
