import pygame
import Car

pygame.init()

info = pygame.display.Info()
# sw = info.current_w
# sh = info.current_h
sw = 1600
sh = 900

# sw = 1200
# sh = 700

size = sw, sh
bg = 15, 15, 30

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Race Track")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

carImg = pygame.image.load("car.png")
firstCar = Car.Car("First car", carImg, 0, 0.95, 0.93, 100, 100)

carImg2 = pygame.image.load("car2.png")
secondCar = Car.Car("Second car", carImg2, 0, 0.98, 0.93, 100, 200)

cars = [firstCar]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            elif event.key == pygame.K_n:
                cars.append(secondCar)
            else:
                for car in cars:
                    car.handle_keydown(event.key)

        if event.type == pygame.KEYUP:
            for car in cars:
                car.handle_keyup(event.key)

    screen.fill(bg)

    for car in cars:
        car.update()

    pygame.display.update()
    clock.tick(60)
