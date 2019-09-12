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
        self.maxSpeed = 6
        self.crashed = False
        self.speeding = False
        self.slowing = False
        self.turningL = False
        self.turningR = False
        self.screen = pygame.display.get_surface()

    def calculate_new_position(self):
        newX = math.cos(math.radians(self.angle))
        newY = math.sin(math.radians(self.angle))

        return self.x + newX * self.speed, self.y - newY * self.speed

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
            self.speeding = True
            self.slowing = False
        elif key == pygame.K_DOWN:
            self.speeding = False
            self.slowing = True

        elif key == pygame.K_LEFT:
            self.turningL = True
            self.turningR = False
        elif key == pygame.K_RIGHT:
            self.turningL = False
            self.turningR = True

    def handle_keyup(self, key):
        print(key)
        if key == pygame.K_UP:
            self.speeding = False
            print("Key up")
        elif key == pygame.K_DOWN:
            self.slowing = False

        elif key == pygame.K_LEFT:
            self.turningL = False
        elif key == pygame.K_RIGHT:
            self.turningR = False

    def handle_movement(self):
        if self.speeding and self.speed <= self.maxSpeed:
            self.change_speed(0.1)
        elif self.slowing and self.speed >= -self.maxSpeed:
            self.change_speed(-0.1)

        if self.turningL:
            self.change_angle(2)
        elif self.turningR:
            self.change_angle(-2)

    def update(self):
        self.handle_movement()
        self.move()

