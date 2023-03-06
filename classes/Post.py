import pygame
import os

import classes.Post
from classes.Comment import Comment

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    user_name = "Adiel_Cohen"

    def __init__(self, location, description):
        # TODO: write me!
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def display(self):

        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        pass

    def display_header(self):
        font = pygame.font.SysFont("chalkduster.ttf", COMMENT_TEXT_SIZE)
        text = font.render(self.location, True, LIGHT_GRAY)
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        font = pygame.font.SysFont("chalkduster.ttf", COMMENT_TEXT_SIZE)
        text = font.render(self.description, True, GREY)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        font = pygame.font.SysFont("chalkduster.ttf", COMMENT_TEXT_SIZE)
        text = font.render(self.user_name, True, GREY)
        screen.blit(text, [USER_NAME_X_POS, USER_NAME_Y_POS])

    def display_likes(self):
        font = pygame.font.SysFont("chalkduster.ttf", COMMENT_TEXT_SIZE)
        text = font.render("Liked by " + str(self.likes_counter) + " users", True, BLACK)
        screen.blit(text, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, user_comment):
        new_comment = Comment(user_comment)  # יצירת אובייקט מסוג תגובה
        self.comments.append(new_comment)

    @staticmethod
    def censor(list_censor, comment):  # adiel shit damm
        real_comment = []
        for word in comment.split():
            if word in list_censor:
                word = len(word) * "*"
                real_comment.append(word)
            else:
                real_comment.append(word)
        return " ".join(real_comment)

    # def Passing_posts(self,):
    # directory = "C:\\Users\\adiel\\PycharmProject\\NIZGRAM\\Images"
    # list_post = []
    # for filename in os.listdir(directory):
    #     full_file_path = os.path.join(directory, filename)
    #     if os.path.isfile(full_file_path) and filename.endswith('.jpg'):
    #         list_post += filename
    #         print(filename)

    # for i in range (len(list_post)):
    #   current_post = Post(list_post[i], "")
    # for i in post_3:
    #   list_post = i
    def display_comments(self):

        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
