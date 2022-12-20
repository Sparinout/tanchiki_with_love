from variables import *

'''Данная часть кода отвечает за отображение текста по ходу игры.'''
def score_draw(score_first_player, score_second_player, f, WIDTH, HEIGHT):
    '''
    Функция отрисовки счёта во время игры.
    score_first_player: счёт первого игрока
    score_second_player: счёт второго игрока
    f: стиль текста
    WIDTH: ширина экрана
    HEIGHT: высота экрана
    '''
    text1 = f.render(str(score_first_player), 1, (255, 0, 0))
    text2 = f.render(str(score_second_player), 1, (0, 0, 255))

    screen.blit(text1, (WIDTH / 2 - 44, 0.05 * HEIGHT))
    screen.blit(text2, (WIDTH / 2 + 34, 0.05 * HEIGHT))


def final_draw(score_first_player, score_second_player, f, WIDTH, HEIGHT):
    '''
    Функция отрисовки текста окончания игры.
    score_first_player: счёт первого игрока
    score_second_player: счёт второго игрока
    f: стиль текста
    WIDTH: ширина экрана
    HEIGHT: высота экрана
    '''
    text1 = f.render('Второй игрок вышел из игры!', 1, (0, 0, 0))
    text2 = f.render('Конечный счёт:', 1, (0, 0, 0))

    text3 = f.render(str(score_first_player), 1, (255, 0, 0))
    text4 = f.render(str(score_second_player), 1, (0, 0, 255))

    screen.blit(text1, (WIDTH / 2 - 305, HEIGHT / 2 - 90))
    screen.blit(text2, (WIDTH / 2 - 160, HEIGHT / 2 - 30))

    screen.blit(text3, (WIDTH / 2 - 80, HEIGHT / 2 + 40))
    screen.blit(text4, (WIDTH / 2 + 60, HEIGHT / 2 + 40))

def click_anywhere_draw(f, WIDTH, HEIGHT):
    '''
    Функция отрисовки надписи (Нажмите в любую часть экрана для завершения игры).
    f: стиль текста
    WIDTH: ширина экрана
    HEIGHT: высота экрана
    '''
    text1 = f.render('(Нажмите в любую часть экрана для завершения игры)', 1, (125, 125, 125))
    screen.blit(text1, (WIDTH / 2 - 222, HEIGHT / 2 + 90))
