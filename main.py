import pygame
import Car

pygame.init()

info = pygame.display.Info()
# sw = info.current_w
# sh = info.current_h
sw = 1600
sh = 900

size = sw, sh
bg = 15, 15, 30

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Race Track")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

carImg = pygame.image.load("car.png")
firstCar = Car.Car("First car", carImg, 0, 0, 100, 100)
# secondCar = Car.Car("Second car", carImg)
# cars =

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            firstCar.handle_keydown(event.key)

        if event.type == pygame.KEYUP:
            firstCar.handle_keyup(event.key)

    screen.fill(bg)
    firstCar.update()
    pygame.display.update()
    clock.tick(60)
