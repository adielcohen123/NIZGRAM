from helpers import screen
import pygame
from constants import *


class Filter:

    def __init__(self, color_filter, level_transparency):
        self.color_filter = color_filter
        self.level_transparency = level_transparency

    def apply_filter(self):
        rect = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        rect.set_alpha(self.level_transparency)
        rect.fill(self.color_filter)
        screen.blit(rect, (POST_X_POS, POST_Y_POS))

