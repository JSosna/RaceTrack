import pygame
import Car
import math


pygame.init()

size = width, height = 1500, 800
bg = 15, 15, 30

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Race Track")

clock = pygame.time.Clock()


carImg = pygame.image.load("car.png")
carRect = carImg.get_rect()


def move_car(degree, x, y):
    car = pygame.transform.rotate(carImg, degree)
    rect = car.get_rect()
    screen.blit(car, (x-(rect.width/2), y-(rect.height/2)))


def rotate_car(degree, x, y):
    car = pygame.transform.rotate(carImg, degree)
    # screen.blit(car, (x, y))


def calculateNewPosition(speed, x, y):
    newX = math.cos(math.radians(degrees))
    newY = math.sin(math.radians(degrees))

    return (x + newX * speed, y - newY * speed)


info = pygame.display.Info()
sw = info.current_w
sh = info.current_h

x = sw * 0.15
y = sh * 0.15

dx = 0.5
dy = 0.2

speed = 0
degrees = 0

left = False
right = False

speedingUp = False
slowingDown = False


firstCar = Car.Car("First car", carImg, 0, 0, 100, 100)


while True:

    if speedingUp and speed < 7:
        speed += 0.1
        firstCar.change_speed(0.1)
    elif slowingDown and speed > -4:
        speed -= 0.1
        firstCar.change_speed(-0.1)
        print(firstCar.speed)

    x, y = calculateNewPosition(speed, x, y)

    if left and (speed > 1 or speed < -1):
        if speed > 1:
            degrees += 2
            firstCar.change_angle(2)
        elif speed < -1:
            degrees -= 2
            firstCar.change_angle(-2)
    elif right and (speed > 1 or speed < -1):
        if speed > 1:
            degrees -= 2
            firstCar.change_angle(-2)
        elif speed < -1:
            degrees += 2
            firstCar.change_angle(2)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speedingUp = True
                slowingDown = False

            elif event.key == pygame.K_DOWN:
                speedingUp = False
                slowingDown = True

            if event.key == pygame.K_LEFT:
                left = True
                right = False

            elif event.key == pygame.K_RIGHT:
                right = True
                left = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speedingUp = False

            elif event.key == pygame.K_DOWN:
                slowingDown = False

            if event.key == pygame.K_LEFT:
                left = False

            elif event.key == pygame.K_RIGHT:
                right = False

        print(event)

    screen.fill(bg)
    # rotate_car(degrees, x, y)
    firstCar.move()
    move_car(degrees, x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
