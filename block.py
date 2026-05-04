import pygame

class Block:
    def __init__(self, player_x1, player_y1, player_x, player_y, x, y, w ,h, color):
        self.x =
        self.y =
        self.body=pygame.Rect(self.x - player_x + 275, self.y - player_y + 275, w, h)
        self.color=color

    def show(self, pg):
        pygame.draw.rect(pg, self.color, self.body)
    def move(self, player_x, player_y):
        self.body.x = self.x - player_x + 275
        self.body.y = self.y - player_y + 275






















