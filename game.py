from pickle import FALSE
from turtle import speed, width
import pygame

pygame.init #инициализируем библиотек , то есть запускаем
win = pygame.display.set_mode((500, 500))#win  переменная служит для нашего окна, в которое запишем хар-ки окна, установили размер окна
pygame.display.set_caption("Cubes")# заголовок 

# переменные
x = 50
y = 50
width = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)
# позволяет установить количесвтво милисекунд, через которое у нас будет выполняться этот цикл

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# научим двигать игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    win.fill((0, 0, 0))#используем множество и предыдущие действия перекрашиваем в черный цвет, что синих квадратов не было пред видно
# нарисуем главного игрока

    pygame.draw.rect(win, (0,0,255), (x, y, width, height))#создали квадрат синего цвета
    pygame.display.update()



pygame.quit()

