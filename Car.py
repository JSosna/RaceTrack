import pygame
import math


class Car:

    def __init__(self, name, steering, car_img, degrees, drag, angular_drag, x, y):
        self.name = name
        self.carImg = car_img
        self.angle = degrees
        self.angular_velocity = 0
        self.angular_drag = angular_drag
        self.turn_speed = 0.2
        self.power = 0
        self.position = pygame.math.Vector2()
        self.position.x = x
        self.position.y = y
        self.velocity = pygame.math.Vector2()
        self.maxSpeed = 0.45
        self.drag = drag
        self.crashed = False
        self.motion = 'n'
        self.brake = False
        self.turn = 'n'
        self.screen = pygame.display.get_surface()

    def calculate_new_position(self):
        self.velocity.x += math.cos(math.radians(self.angle)) * self.power
        self.velocity.y += math.sin(math.radians(self.angle)) * self.power

        return self.position.x + self.velocity.x, self.position.y - self.velocity.y

    def move(self):
        self.position.x, self.position.y = self.calculate_new_position()
        rotation = pygame.transform.rotate(self.carImg, self.angle)
        rect = rotation.get_rect()
        self.screen.blit(rotation, (self.position.x - (rect.width / 2), self.position.y - (rect.height / 2)))

    def change_power(self, value):
        self.power += value

    def change_angle(self, value):
        self.angular_velocity += value

    def handle_key_down(self, key):
        if key == pygame.K_UP:
            self.motion = '+'
        elif key == pygame.K_DOWN:
            self.motion = '-'
        elif key == pygame.K_SPACE:
            self.brake = True

        elif key == pygame.K_LEFT:
            self.turn = 'l'
        elif key == pygame.K_RIGHT:
            self.turn = 'r'

    def handle_key_up(self, key):
        if (key == pygame.K_UP and self.motion == '+') or (key == pygame.K_DOWN and self.motion == '-'):
            self.motion = 'n'

        elif key == pygame.K_SPACE:
            self.brake = False

        elif (key == pygame.K_LEFT and self.turn == 'l') or (key == pygame.K_RIGHT and self.turn == 'r'):
            self.turn = 'n'

    def handle_movement(self):
        self.angle += self.angular_velocity
        self.angular_velocity *= self.angular_drag
        self.velocity *= self.drag

        # Speeding up, down
        if self.motion == '+' and self.power <= self.maxSpeed:
            self.change_power(0.005)
        elif self.motion == '-' and self.power >= -self.maxSpeed/3:
            self.change_power(-0.005)

        # Breaking
        if self.brake and self.velocity.x != 0 and self.velocity.y != 0:
            # self.velocity *= 0.97
            self.power *= 0.93

        # Turning
        if self.turn == 'l':
            if self.power > 0.05:
                self.change_angle(self.turn_speed)
            elif self.power < -0.05:
                self.change_angle(-self.turn_speed)
        elif self.turn == 'r':
            if self.power > 0.05:
                self.change_angle(-self.turn_speed)
            elif self.power < -0.05:
                self.change_angle(self.turn_speed)

    def update(self):
        self.handle_movement()
        self.move()
