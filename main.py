import pygame
import requests
import sys, os


class Map(object):
    def __init__(self, dolg, shir, a1, a2):
        self.dolgota = dolg
        self.shirina = shir
        self.mashtab1 = a1
        self.mashtab2 = a2
        self.type = 'map'

    def ll(self):
        return str(self.dolgota) + ',' + str(self.shirina)

    def coor(self):
        return str(self.mashtab1) + ',' + str(self.mashtab2)


def load(map):
    ll = map.ll()
    coord = map.coor()
    type = map.type

    map_req = f'http://static-maps.yandex.ru/v1/?ll={ll}&z={coord}&l={type}'
    response = requests.get(map_req)
    map_file = 'map.png'
    try:
        with open(map_file, 'wb') as file:
            file.write(response.content)
    except Exception:
        print('ошибка')
    return map_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    map = Map(61.665279, 50.813492, 0.0001, 0.0001)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        map_file = load(map)
        screen.blit(pygame.image, load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    main()