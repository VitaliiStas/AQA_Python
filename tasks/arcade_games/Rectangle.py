import random

import pygame


class Rectangle:
    x = 0
    y = 0
    width = 10
    height = 10
    change_x = 2
    change_y = 2
    color = RED = (255, 0, 0)

    def __init__(self):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)
        self.change_x = random.randrange(-3., 3)
        self.change_y = random.randrange(-3., 3)
        self.width = random.randrange(20, 70)
        self.height = random.randrange(20, 70)
        self.color = [random.randrange(0, 256) for _ in range(3)]


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 0)

    def move(self):
        if self.x < 0:
            self.change_x *= -1
        if self.x > 700-self.width:
            self.change_x *= -1
        if self.y < 0:
            self.change_y *= -1
        if self.y > 500-self.height:
            self.change_y *= -1
        self.x += self.change_x
        self.y += self.change_y
