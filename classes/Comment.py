import pygame
from constants import *
from helpers import screen


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        font = pygame.font.SysFont('chalkduster.ttf', 15)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + COMMENT_LINE_HEIGHT * comment_num])
