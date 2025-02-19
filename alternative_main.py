import os
import sys

import pygame
import requests

api_server = 'https://static-maps.yandex.ru/v1/'

par = {
    'apikey': 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13',
    'll': ','.join(['55', '48']),
    'spn': ','.join(['0.01', '0.01']),
    'l': 'sat'
}

response = requests.get(api_server, params=par)
print(response.content)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
