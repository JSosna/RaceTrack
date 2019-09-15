import pygame
from car import Car
from map import Map
from client import Client


class Game:

    def __init__(self, size, chosen_map):
        self.client = Client('localhost', 8080)
        self.size = size
        self.cars = []
        self.current_map = Map("Current map", chosen_map)
        self.bg = 120, 180, 120
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)

    def load_game(self):
        pygame.display.set_caption("Race Track")
        pygame.mouse.set_visible(False)

        car_img = pygame.image.load("car.png")
        car_sized = pygame.transform.rotozoom(car_img, 0, 0.5)
        car1 = Car("First car", car_sized, 0, 0.95, 0.93, 100, 100)
        self.cars.append(car1)

        car_img2 = pygame.image.load("car2.png")
        car_sized2 = pygame.transform.rotozoom(car_img2, 0, 0.5)
        car2 = Car("Second car", car_sized2, 0, 0.95, 0.93, 100, 200)
        self.cars.append(car2)

        self.run()

    def send_data(self):
        data = str(self.client.id) + ":" + str(self.cars[0].position.x) + "," + str(self.cars[0].position.y)
        reply = self.client.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            if data:
                d = data.split(":")[1].split(",")
                print(d)
                return int(float(d[0])), int(float(d[1]))
        except TypeError as err:
            print("Error while splitting data in function 'parse_data'" + str(err))

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

            self.cars[1].position.x, self.cars[1].position.y = self.parse_data(self.send_data())

            self.screen.fill(self.bg)
            self.current_map.update()
            for car in self.cars:
                car.update()

        pygame.quit()
