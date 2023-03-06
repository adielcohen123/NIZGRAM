from classes.Post import Post
from constants import *
import pygame
from pygame import *

from helpers import screen
from classes.Filter import Filter


class Image_Post(Post):  # - inheritance
    def __init__(self, image_src, location, description, filter =None):
        Post.__init__(self, location, description)  # operating
        self.filter = filter
        self.img = pygame.image.load(image_src)
        self.img = pygame.transform.scale(self.img, (POST_WIDTH, POST_HEIGHT))

    def display_content(self):
        screen.blit(self.img, (POST_X_POS, POST_Y_POS))
        if self.filter != None:
            self.filter.apply_filter()

        # rect = pygame.Surface((180, 150))
        # rect.set_alpha(220)
        # rect.fill((100, 200, 40))
        # screen.blit(rect, (POST_X_POS, POST_Y_POS))
