from tkinter import *
from random import randint
from time import sleep

# Очистить всё и начать игру заново
def continieAfterPause():
    pass

# Запись очков в файл
def endTableScore(inputWindow, positionPlayer):
    pass

# Фильтрация вводимых знаков
def inputNameFilner(event):
    pass

# Окно для ввода имени
def getPlayerName(positionPlayer):
    pass

# Находим номер игрока в списке лучших
def sortScoreTable(score):
    pass

# Конец игры
def endGame():
    pass

# Геттер - координата X инопланетянина obj
def getInvadersX(obj):
    pass

# Геттер - координата Y инопланетянина obj
def getInvadersY(obj):
    pass

# Геттер - координата X корабля игрока
def getPlayerX():
    pass

# Геттер - координата Y корабля игрока
def gePlayerY():
    pass

# Геттер - координата X ракеты
def getRocketX():
    pass

# Геттер - координата Y ракеты
def getRocketY():
    pass

# Обновляем инфостроку
def updateInfoLine():
    pass

# Запись очков в файл
def saveScores(scoresToFile):
    pass

# Загрузка очков из scores.dat
def loadScores():
    pass

# Удаляем таблицу очков
def hideScores():
    pass

# Рисуем таблицу очков
def showScores(numberPlayer):
    pass

# Показываем кнопки меню
def showMenu():
    pass

# Скрываем кнопки меню
def hideMenu():
    pass

# Анимация вражеской ракеты
def animationInvadersRocket():
    pass

# Стартуем ракету врага
def startInvadersRocket():
    pass

# Анимация взрыва
def animationExplosion(frame, x, y):
    pass

# Старт анимации взрыва
def startExplosion(n):
    pass

# Анимация ракеты
def animationShot(frame):
    pass

# При нажатии на пробел выстрел
def shoot():
    pass

# Перемещение игрока
def move(x):
    pass

# Переключение на следующий уровень
def nextLevel():
    pass

# Конец уровня
def endLevel():
    pass

# Главный цикл игры
def mainloop():
    pass

# Нажатие на кнопку старт
def startGame():
    pass

# Сброс всего под чистую с установкой первого уровня
def globalReset():
    pass

# Перезапуск игры полностью
def restartGame():
    pass

# Сброс и формирование объектов игрового мира
def reset():
    pass

# ++++++++++++++++++++ Основной блок программы +++++++++++++++

# Созданаие окна
root = Tk()
root.resizable(False, False)
root.title("Вторжение инопланетян")
root.iconbitmap("icon/icon.ico")

# Геометрия окна
WIDTH = 800
HEIGHT = 480
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() //2 - HEIGHT //2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Канвас
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)

# Текстура фона
backGround = PhotoImage(file="image/background.png")



root.mainloop()



