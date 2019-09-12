import pygame
import math


class Car:

    def __init__(self, name, carImg, degrees, speed, x, y):
        self.name = name
        self.carImg = carImg
        self.angle = degrees
        self.speed = speed
        self.x = x
        self.y = y
        self.crashed = False
        self.screen = pygame.display.get_surface()

    def calculate_new_position(self):
        newX = math.cos(math.radians(self.angle))
        newY = math.sin(math.radians(self.angle))

        return (self.x + newX * self.speed, self.y - newY * self.speed)

    def move(self):
        self.x, self.y = self.calculate_new_position()
        rotation = pygame.transform.rotate(self.carImg, self.angle)
        rect = rotation.get_rect()
        self.screen.blit(rotation, (self.x - (rect.width / 2), self.y - (rect.height / 2)))

    def change_speed(self, value):
        self.speed += value

    def change_angle(self, value):
        self.angle += value
