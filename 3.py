from random import randint
import pygame

WIDTH = 1200
HEIGHT = 600
pygame.init()
pygame.display.set_caption('Фрактал')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
fps = 7
c = ((600, 100), (400, 500), (800, 500))
running = True

clock = pygame.time.Clock()


def game():
    global running, fps
    x = ''
    fps = 7
    running = True
    pygame.display.flip()
    while running:
        while not x:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    x = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x = (event.pos[0], event.pos[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    screen.fill((255, 255, 255))
                    game()
                    running = False
                if event.button == 4:
                    fps += 1
                if event.button == 5:
                    if fps != 0:
                        fps -= 1
        if running:
            pygame.draw.circle(screen, (0, 0, 0), x, 1)
            i = randint(0, 2)
            x = ((c[i][0] + x[0]) // 2, (c[i][1] + x[1]) // 2)
            pygame.display.flip()
            clock.tick(fps)


game()
pygame.quit()
