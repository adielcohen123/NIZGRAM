from classes.Post import Post
from constants import *
from helpers import *
from pygame import *


class Text_Post(Post):

    def __init__(self, location, description, background_color, Text, text_color):
        Post.__init__(self, location, description)
        self.background_color = background_color
        self.Text = Text
        self.text_color = text_color
        self.text_array = from_text_to_array(Text)

    def display_content(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        for i in range(len(self.text_array)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text_array[i], True, self.text_color)
            screen.blit(text, center_text(len(self.text_array), text, i))

