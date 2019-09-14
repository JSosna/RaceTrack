import pygame
from car import Car
from map import Map
from client import Client


class Game:

    def __init__(self, size, chosen_map):
        self.client = Client('localhost', '8080')
        self.size = size
        self.cars = []
        self.players = []
        self.current_map = Map("Current map", chosen_map)
        self.bg = 120, 180, 120
        self.screen = pygame.display.get_surface()

    def load_game(self):
        screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        pygame.display.set_caption("Race Track")
        pygame.mouse.set_visible(False)

        car_img = pygame.image.load("car.png")
        car_sized = pygame.transform.rotozoom(car_img, 0, 0.5)
        self.cars.append(car_sized)

        car_img2 = pygame.image.load("car2.png")
        car_sized2 = pygame.transform.rotozoom(car_img2, 0, 0.5)
        self.cars.append(car_sized2)

        self.update()

    def add_player(self, car):
        pass


    def run(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    else:
                        for car in self.cars:
                            car.handle_key_down(event.key)

                if event.type == pygame.KEYUP:
                    for car in self.cars:
                        car.handle_key_up(event.key)

            self.screen.fill(self.bg)
            self.current_map.update()
            for car in cars:
                car.update()
