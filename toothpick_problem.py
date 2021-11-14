from typing import Tuple

import pygame, sys
import operator


SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE= (0, 0, 255)
RED = (200, 0, 0 )
LIGHTRED= (255, 100, 100)
PURPLE = (102, 0, 102)
LIGHTPURPLE = (153, 0, 153)


def stuple(a, b):
    return tuple(map(operator.add, a, b))


def main():
    size = width, height = (2560, 1440)

    tsize = 2  # toothpick size
    thick = 1  # thickness of toothpicks

    origin = width // 2, height // 2
    left, right, up, down = (-tsize // 2, 0), (tsize // 2, 0), (0, -tsize // 2), (0, tsize // 2)

    step = 0
    steps = 10140000
    colors = (LIGHTPURPLE, LIGHTPURPLE)
    points = {stuple(origin, up), stuple(origin, down)}

    pygame.init()
    screen = pygame.display.set_mode(size=size, flags=pygame.FULLSCREEN)

    pygame.draw.line(screen, colors[1], stuple(origin, up), stuple(origin, down), thick)

    clock = pygame.time.Clock()
    screen.fill(SHADOW)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                pass

        if step <= steps:
            p2 = set()
            for point in points:
                v1, v2 = None, None
                if step %  2 == 0:
                    v1, v2 = stuple(point, left), stuple(point, right)
                else:
                    v1, v2 = stuple(point, down), stuple(point, up)

                if p2.__contains__(v1):
                    p2.remove(v1)
                else:
                    p2.add(v1)
                if p2.__contains__(v2):
                    p2.remove(v2)
                else:
                    p2.add(v2)

                pygame.draw.line(screen, colors[step % 2], v1, v2, thick)

            points = p2
            step += 1

        pygame.display.flip()
        #clock.tick(1)


if __name__ == '__main__':
    main()
