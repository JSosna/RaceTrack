from game import Game
from map import Map
import pygame


sw = 1600
sh = 900

size = sw, sh
bg = 120, 180, 120


if __name__ == '__main__':
    pygame.init()

    mapImg = pygame.image.load("track1s.png")
    mapSized = pygame.transform.scale(mapImg, (1600, 900))
    firstMap = Map("First", mapSized)
    game = Game(size, firstMap)
    game.load_game()
