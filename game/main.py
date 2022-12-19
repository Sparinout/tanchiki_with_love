import numpy as np

from gun import *
from tank import *
from client import *
from text import *
import time

connection = '0'

while connection != '1':
    try:
        connection = sock.recv(2048).decode()
    except:
        pass
    time.sleep(1)

# Класс Ball уже импортирован в gun, внешние библиотеки содержатся в variables,
# который, в свою очередь уже используется в других файлах с классами
player = 0

# Создание объектов класса Tank и Gun
for i in range(number_of_tanks):
    t = Tank(screen)
    if i >= 1:
        t.color = BLUE
    tanks.append(t)
    t.draw()
    g = Gun(screen)
    guns.append(g)

# Основная часть программы
while not finished:
    # Далее описан один период выполнения программы, время периода -- 1/FPS
    screen.fill((255, 255, 255))
    # Движение и прорисовка снарядов
    for b in balls:
        for i in range(1, len(tanks)):
            if b.hittest(tanks[i]):

                score_first_player += 1
                balls.pop(balls.index(b))
            else:
                b.move()
                b.draw()

    # Прорисовка корпуса танка и пушки
    for i in range(number_of_tanks):
        tanks[i].draw()
        guns[i].draw(tanks[i].x + tanks[i].width / 2, tanks[i].y + tanks[i].height / 2)
        tanks[i].draw_turret()
    # Проверка происходящих событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                tanks[player].right_on = 1
            if event.key == pygame.K_a:
                tanks[player].left_on = 1
            if event.key == pygame.K_w:
                tanks[player].up_on = 1
            if event.key == pygame.K_s:
                tanks[player].down_on = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                tanks[player].right_on = 0
            if event.key == pygame.K_a:
                tanks[player].left_on = 0
            if event.key == pygame.K_w:
                tanks[player].up_on = 0
            if event.key == pygame.K_s:
                tanks[player].down_on = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            guns[player].fire2_start()
        if event.type == pygame.MOUSEBUTTONUP:
            guns[player].fire2_end(event,
                                   tanks[player].x + tanks[player].width / 2 + guns[player].l * np.cos(guns[player].an),
                                   tanks[player].y + tanks[player].height / 2 + guns[player].l * np.sin(
                                       guns[player].an))
        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
    # Движение танка
    tanks[player].move()
    guns[player].targetting(mouse_x, mouse_y,
                            tanks[player].x + tanks[player].width / 2, tanks[player].y + tanks[player].height / 2)
    # Создаем строку с координатами нашего танка
    data_send = str(tanks[player].x) + ' ' + str(tanks[player].y) + ' ' + str(guns[player].an) + ' ' + str(
        score_first_player) + ' '
    # Добавляем к строке координаты шариков
    for b in balls:
        data_send += str(b.x) + ' ' + str(b.y) + ' '
    # Отправляем строку на сервер
    send(data_send)
    # Принимаем строку данных от сервера
    data_recv = receive()
    # Если второй игрок отключился, сервер отправляет игроку специальную команду, распознание которой осуществляет if ниже
    if data_recv[0] == 2.0:
        finished = True
        screen.fill((255, 255, 255))
        final_draw(score_first_player, score_second_player, f2, WIDTH, HEIGHT)
        click_anywhere_draw(f3, WIDTH, HEIGHT)
        pygame.display.update()
        flag = True
        while flag:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.QUIT:
                    flag = False
    else:
        # Обработка полученных данных
        for another_player in range(1, number_of_tanks):
            tanks[another_player].x = WIDTH - tanks[another_player].width - data_recv[0]
            tanks[another_player].y = HEIGHT - tanks[another_player].height - data_recv[1]
            guns[another_player].an = data_recv[2] + np.pi
            score_second_player = int(data_recv[3])
            for i in range(5, len(data_recv), 2):
                circle_draw(screen, BLUE, WIDTH - data_recv[i - 1], HEIGHT - data_recv[i], 5)
        # Отрисовка счёта
        score_draw(score_first_player, score_second_player, f1, WIDTH, HEIGHT)
        # Обновление дисплея
        pygame.display.update()

disconnection_flag()
pygame.quit()
