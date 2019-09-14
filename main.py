import pygame
import car
import map
import game

pygame.init()

info = pygame.display.Info()
# sw = info.current_w
# sh = info.current_h
sw = 1600
sh = 900

# sw = 1200
# sh = 700

size = sw, sh
bg = 120, 180, 120

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Race Track")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

mapImg = pygame.image.load("track1s.png")
mapSized = pygame.transform.scale(mapImg, (1600, 900))
firstMap = map.Map("First", mapSized)

carImg = pygame.image.load("car.png")
carSized = pygame.transform.rotozoom(carImg, 0, 0.5)
firstCar = car.Car("First car", carSized, 0, 0.95, 0.93, 100, 100)

carImg2 = pygame.image.load("car2.png")
carSized2 = pygame.transform.rotozoom(carImg2, 0, 0.5)
secondCar = car.Car("Second car", carSized2, 0, 0.95, 0.93, 100, 200)

cars = [firstCar]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            elif event.key == pygame.K_n:
                if(len(cars) == 1):
                    cars.append(secondCar)
            else:
                for car in cars:
                    car.handle_key_down(event.key)

        if event.type == pygame.KEYUP:
            for car in cars:
                car.handle_key_up(event.key)

    screen.fill(bg)
    firstMap.update()
    for car in cars:
        car.update()

    pygame.display.update()
    clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.load_game(1)
