import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Post import *
from test_methods import *
from buttons import like_button
from buttons import comment_button
from buttons import click_post_button
from classes.ImagePost import Image_Post
from classes.TextPost import Text_Post
from classes.Filter import Filter



def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    text_post = Text_Post("Israel", "This is Text Post on Nitzagram!!",(71, 144, 205),
                         "ohad hagever", (216, 79, 81) )


    # TODO: add a post here

    current_post = Image_Post("Images/noa_kirel.jpg", "netivot", "party")  # יצירת אובייקט מסוג פוסט
    filter_ = Filter((30, 12, 121), 80)
    post_1 = Image_Post("Images/noa_kirel.jpg", "netivot", "party", filter_)
    post_2 = Image_Post("Images/ronaldo.jpg", "beer sheva", "not party")
    list_post = [post_1, post_2, text_post]
    current_index = 0
    current_post = list_post[current_index]

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # מיקום לחיחצת העכבר
                if mouse_in_button(comment_button, pos):
                    user_comment = read_comment_from_user()
                    Post.censor(["shit", "damm"], user_comment)
                    user_comment = Post.censor(["shit", "damm"], user_comment)
                    current_post.add_comment(user_comment)
                if mouse_in_button(like_button, pos):
                    current_post.add_like()

                if mouse_in_button(click_post_button, pos):
                    current_post = list_post[current_index]
                    if current_index < (len(list_post)) - 1:
                        current_index += 1
                    elif current_index == (len(list_post) - 1):
                        current_index = 0

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
