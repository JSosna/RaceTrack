import pygame
import math


class Car:

    def __init__(self, name, car_img, degrees, speed, x, y):
        self.name = name
        self.carImg = car_img
        self.angle = degrees
        self.speed = speed
        self.x = x
        self.y = y
        self.maxSpeed = 6
        self.rotation = 2
        self.crashed = False
        self.motion = 'n'
        self.turn = 'n'
        self.screen = pygame.display.get_surface()

    def calculate_new_position(self):
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))

        return self.x + dx * self.speed, self.y - dy * self.speed

    def move(self):
        self.x, self.y = self.calculate_new_position()
        rotation = pygame.transform.rotate(self.carImg, self.angle)
        rect = rotation.get_rect()
        self.screen.blit(rotation, (self.x - (rect.width / 2), self.y - (rect.height / 2)))

    def change_speed(self, value):
        self.speed += value

    def change_angle(self, value):
        self.angle += value

    def handle_keydown(self, key):
        if key == pygame.K_UP:
            self.motion = '+'
        elif key == pygame.K_DOWN:
            self.motion = '-'

        elif key == pygame.K_LEFT:
            self.turn = 'l'
        elif key == pygame.K_RIGHT:
            self.turn = 'r'

    def handle_keyup(self, key):
        if (key == pygame.K_UP and self.motion == '+') or (key == pygame.K_DOWN and self.motion == '-'):
            self.motion = 'n'

        elif (key == pygame.K_LEFT and self.turn == 'l') or (key == pygame.K_RIGHT and self.turn == 'r'):
            self.turn = 'n'

    def handle_movement(self):
        if self.motion == '+' and self.speed <= self.maxSpeed:
            self.change_speed(0.1)
        elif self.motion == '-' and self.speed >= -self.maxSpeed:
            self.change_speed(-0.1)

        if self.turn == 'l':
            if self.speed > 1.1:
                self.change_angle(self.rotation)
            elif self.speed < -1.1:
                self.change_angle(-self.rotation)
        elif self.turn == 'r':
            if self.speed > 1.1:
                self.change_angle(-self.rotation)
            elif self.speed < -1.1:
                self.change_angle(self.rotation)

    def update(self):
        self.handle_movement()
        self.move()
