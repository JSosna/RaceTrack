import pygame

class Map:

    def __init__(self, name, map_image):
        self.name = name
        self.map_image = map_image
        self.screen = pygame.display.get_surface()

    def print_map(self):
        if self.screen:
            self.screen.blit(self.map_image, (0, 0))

    def update(self):
        self.print_map()
