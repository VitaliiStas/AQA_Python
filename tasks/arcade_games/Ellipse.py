import pygame

from tasks.arcade_games.Rectangle import Rectangle


class Ellipse(Rectangle):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height], 0)