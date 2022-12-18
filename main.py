from gun import *
from tank import *
from client import *
import time

connection = '0'

while connection != '1':
    try:
        connection = sock.recv(1024).decode()
    except:
        pass
    time.sleep(1)

# Класс Ball уже импортирован в gun, внешние библиотеки содержатся в variables,
# который, в свою очередь уже используется в других файлах с классами
player = 0

# Создание объектов класса Tank и Gun
for i in range(number_of_tanks):
    t = Tank(screen)
    tanks.append(t)
    t.draw()
    g = Gun(screen)
    guns.append(g)

# Основная часть программы
while not finished:
    # Далее описан один период выполнения программы, время периода -- 1/FPS
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    # Движение и прорисовка снарядов
    for b in balls:
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
    # Обновление дисплея
    pygame.display.update()
    # Создаем строку с координатами нашего танка
    data_send = str(tanks[player].x) + ' ' + str(tanks[player].y) + ' ' + str(guns[player].an) + ' '
    # Добавляем к строке координаты шариков
    for b in balls:
        data_send += str(b.x) + ' ' + str(b.y) + ' '
    # Отправляем строку на сервер
    send(data_send)
    # Принимаем строку данных от сервера
    try:
        s = sock.recv(1024).decode()
        data_recv = list(map(float, s.split()))
        for another_player in range(1, number_of_tanks):
            tanks[another_player].x = data_recv[0]
            tanks[another_player].y = data_recv[1]
            guns[another_player].an = data_recv[2]
            tanks[another_player].draw()
            guns[another_player].draw(tanks[another_player].x + tanks[another_player].width / 2,
                                      tanks[another_player].y + tanks[another_player].height / 2)
    except:
        pass
    # Прорисовка танка и шаров другого игрока
pygame.quit()