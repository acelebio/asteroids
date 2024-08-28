# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *


def main():
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    dt = 0
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        surface=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.Surface.fill(surface,(255,255,0))
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
        main()
