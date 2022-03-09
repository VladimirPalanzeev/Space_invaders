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
    return cnv.coords(player[0])[0]

# Геттер - координата Y корабля игрока
def getPlayerY():
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
def animationShoot(frame):
    global rocketObject, rocketSpeedY, penalty, score, player

    if not playGame:
        rocketObject = None
        rocketSpeedY = rocketSpeedYDefault
        return 0

    cnv.move(rocketObject, 0, -rocketSpeedY)
    rocketSpeedY *= rocketScale

    x = getRocketX()
    y = getRocketY()

    frame += 1
    if frame > len(rocketTexture) - 1:
        frame = 0
        sleep(0.02)
    # Удаляем объект и создаем с новой текстурой
    cnv.delete(rocketObject)
    rocketObject = cnv.create_image(x, y, image=rocketTexture[frame])

    if cnv.coords(rocketObject)[1] < maxY + SQUARE_SIZE:
        rocketX = getRocketX()
        rocketY = getRocketY()
        find = 0
        while (find < len(invadersObject)):
            invadersX = getInvadersX(invadersObject[find])
            invadersY = getInvadersY(invadersObject[find])
            # Коэффициент 0.4 - чем меньше, тем точнее надо попасть
            if abs(invadersX - rocketX) < SQUARE_SIZE * 0.4 and abs(invadersY - rocketY) < SQUARE_SIZE * 0.8:
                score += 50
                startExplosion(find)
                y = -1
                find = len(invadersObject)
                penalty -= 5
                find += 1
    if y > 0:
        # Рекурсивно вызываем анимацию
        root.after(3, lambda frame=frame: animationShoot(frame))
    else:
        # Удаляем ракету по окончании анимации
        cnv.delete(rocketObject)
        # Увеличиваем штраф, независимо от попадания
        # P.S. Уменьшаем штраф на 5, когда ракета поразила цель
        penalty += 5
        player[1] += 1
        rocketSpeedY =rocketSpeedYDefault


# При нажатии на пробел - выстрел
def shoot():
    global player, rocketObject
    if not playGame or onMenu:
        return 0
    if (player[1] == 0):
        return 0
    player[1] -= 1

    rocketObject = cnv.create_image(getPlayerX(), getPlayerY(), image=rocketTexture[0])
    root.after(10, lambda frame=0: animationShoot(frame))

# Перемещение игрока
def move(x):
    if not playGame or onMenu:
        return 0
    if x == LEFTKEY:
        cnv.move(player[0], -playerSpeed, 0)
    elif x == RIGHTKEY:
        cnv.move(player[0, playerSpeed, 0])
    if getPlayerX() < SQUARE_SIZE:
        cnv.move(player[0], playerSpeed, 0)
    elif getPlayerX() > WIDTH - SQUARE_SIZE:
        cnv.move(player[0], -playerSpeed, 0)

# Переключение на следующий уровень
def nextLevel():
    global level, playGame
    cnv.delete(ALL)
    level += 1
    playGame = True
    reset()

# Конец уровня
def endLevel():
    global playGame
    playGame = False
    cnv.delete(ALL)
    cnv.create_text(WIDTH // 2, HEIGHT // 2, fill="#ffffff", font=f", 15",
                    text=f"ПОБЕДА! ЗАГРУЖАЕМ СЛЕДУЮЩИЙ УРОВЕНЬ")
    # Забираем фокус с Canvas чтобы не работали кнопки
    root.focus_set()
    root.update()
    sleep(0.01)
    root.after(300, nextLevel)

# Главный цикл игры
def mainloop():
    global invadersObject, leftInvadersBorder, rightInvadersBorder, invadersSpeed, playGame, score, maxY, frame

    # Если список врагов пуст, то есть они все уничтожены
    if len(invadersObject) == 0:
        endLevel()
    # Не выполняем mainloop если нет игры
    if not playGame:
        return 0

    # Перерисовываем текстуры
    for obj in invadersObject:
        cnv.move(obj[0], int(invadersSpeed), 0)
        xPos = getInvadersX(obj)
        yPos = getInvadersY(obj)
        cnv.delete(obj[0])
        obj[0] = cnv.create_image(xPos, yPos, image=invadersTexture[obj[1] * 2 + frame])
    #  Меняем кадр
    frame += 1
    if frame > 1:
        frame = 0

    # Изменяем левую и правую границу инопланетного массива
    leftInvadersBorder += int(invadersSpeed)
    rightInvadersBorder += int(invadersSpeed)

    # Запуск ракеты инопланетян
    if (randint(0, 150)) < abs(invadersSpeed) and invadersRocket == None:
        startInvadersRocket()

    # Проверяем для изменения направления движения самую левую точку X
    # и самую правую точку X прямоугольного блока с инопланетянами
    if rightInvadersBorder > WIDTH - SQUARE_SIZE or leftInvadersBorder < SQUARE_SIZE:
        invadersSpeed *= 1.1
        invadersSpeed = -invadersSpeed
        maxY = 0
        # Перебираем все элементы, т.к. нижние линии в какой-то момент могут быть уничтожены. Поэтому недостаточно
        # взять координату "нижних" элементов математически,
        # умножив размер спрайта на количество линий инопланетных кораблей
        for obj in invadersObject:
            cnv.move(obj[0], 0, SQUARE_SIZE)
            # Находим максимально "нижнюю" точку блока инопланетян
            if cnv.coords(obj[0])[1] + SQUARE_SIZE // 2 > maxY:
                maxY = cnv.coords(obj[0])[1] + SQUARE_SIZE // 2

    # Скорость обновления главного цикла: 100 миллисекунд, то есть 10 (десять) кадров в секунду
    root.after(100, mainloop)
    score -= .1
    updateInfoLine()

    # Если инопланетяне придавили игрока или жизней не осталось совсем
    if maxY > getPlayerY() or lives < 0:
        endGame()

# Нажатие на кнопку старт
def startGame():
    global playGame
    if playGame:
        hideMenu()
        return 0
    playGame = True
    hideMenu()
    mainloop()

# Сброс всего под чистую с установкой первого уровня
def globalReset():
    global level, score, penalty, playGame, playerSpeed, lives
    playGame = False
    playerSpeed = 5
    level = 1
    score = 0
    penalty = 0
    lives = 3

# Перезапуск игры полностью
def restartGame():
    globalReset()
    reset()
    showScores(-1)

# Сброс и формирование объектов игрового мира
def reset():
    global invadersObject, invadersWidth, invadersHeight, invadersSpeed, leftInvadersBorder, rightInvadersBorder,\
        player, maxY, rocketObject, invadersRocket

    cnv.delete(ALL)                                               # Очищаем канвас
    cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)   # Создаем фон (нижний слой)
    cnv.focus_set() # Устанавливаем фокус для перехвата нажатий клавиш на клавиатуре

    rocketObject = None            # Игрок не пустил ракету
    invadersRocket = None          # Инопланетянин не пустил ракету
    invadersSpeed = 3 + level // 5 # Рассчитываем скорость движения инопланетян

    # Рассчитываем количество инопланетян по ширине и высоте
    invadersWidth = (1 + int(level // 3)) * 2
    invadersHeight = 2 + (level // 4)
    if invadersWidth > 14:
        invadersWidth = 14
    if invadersHeight > 8:
        invadersHeight = 8

    # Рассчитываем максимальную точку Y (нижняя линия блока инопланетян). Необходимо, по тому что последующие
    # расчеты происходят по мере смещения инопланетян по Y
    maxY = (invadersHeight - 1) * 10 + SQUARE_SIZE * invadersHeight + SQUARE_SIZE // 2

    invadersObject = []
    for i in range(invadersWidth):
        for j in range(invadersHeight):
            # Уровень врага: 0 - слабый, 2 - сильный
            rang = randint(0, level // 8)
            if rang > 2:
                rang = 2
            posX = SQUARE_SIZE // 2 + (WIDTH // 2 - (invadersWidth * (SQUARE_SIZE + 10)) // 2) + \
                   i * SQUARE_SIZE + i * 10
            posY = 20 + j * 10 + j * SQUARE_SIZE
            # rang умножаем на 2 потому что каждая вторая текстура - текстура для анимации,
            # то есть нужны только изображения по индексам 0, 2, 4
            invadersObject.append([cnv.create_image(posX, posY, image=invadersTexture[rang * 2]), rang])

    # Вычисляем левую и правую границы блока инопланетян:
    # левая - координаты объекта в списке с индексом [0] (левый верхний инопланетянин)
    # правая граница - координаты последнего объекта (правый нижний инопланетянин)
    leftInvadersBorder = cnv.coords(invadersObject[0][0])[0]
    rightInvadersBorder = cnv.coords(invadersObject[len(invadersObject) - 1][0])[0]

    # Космический корабль игрока на Canvas и количество выстрелов
    player = [cnv.create_image(WIDTH // 2, HEIGHT - SQUARE_SIZE * 2, image=playerTexture), 1]

    updateInfoLine()  # Обновляем информационный текст внизу экрана
    mainloop()        # Запускаем игру

# ++++++++++++++++++++ Основной блок программы +++++++++++++++

# Создание окна
root = Tk()
root.resizable(False, False)
root.title("Вторжение инопланетян")
root.iconbitmap("icon/icon.ico")

# Геометрия окна
WIDTH = 800
HEIGHT = 480
SQUARE_SIZE = 32                                     # Размер одного спрайта
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() //2 - HEIGHT //2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Канвас
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)

# Текстура фона
backGround = PhotoImage(file="image/background.png")

# ++++++++++++++++++++ ИНОПЛАНЕТЯНЕ ++++++++++++++++++++++
# Имена файлов с текстурами инопланетян
invadersFile = ["inv01.png", "inv01_move.png",
                "inv02.png", "inv02_move.png",
                "inv03.png", "inv03_move.png"]

# Загружаем текстуры
invadersTexture = []
for fileName in invadersFile:
    invadersTexture.append(PhotoImage(file=f"image/{fileName}"))

# Список информационных объектов
# Индекс [0] - Текстура
# Индекс [1] - Уровень
invadersObject = None
invadersSpeed = None

leftInvadersBorder = None   # Левая и
rightInvadersBorder = None  # Правая границы блока инопланетян в пикселях Необходимо для смены движения

maxY = None # Самая нижняя точка Y расположения текстур инопланетян
invadersWidth = None   # Количество столбцов инопланетян
invadersHeight = None  # Количество строк инопланетян

# ======================== ИГРОК =========================
playerTexture = PhotoImage(file="image/player.png") # Текстура корабля игрока
player = None                                       # Объект для игрока на Canvas
playerSpeed = None                                  # Скорость смещения при нажатии на клавишу управления курсором

# Константы-коды для направления движения
LEFTKEY = 0
RIGHTKEY = 1

# Назначаем клавиши управления
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))
cnv.bind("<space>", lambda e: shoot())
cnv.bind("<Escape>", lambda e: showMenu())

# Спрайты ракеты, выпускаемой инопланетянами
invadersRocketTexture = PhotoImage(file="image/rocket/rocket_invaders.png")
invadersRocket = None                              # Объектна Canvas инопланетной ракеты
invadersRocketSpeedScale = 1.05                    # Увеличение скорости с каждым кадром
invadersRocketSpeedDefault = 1                     # Скорость по умолчанию
invadersRocketSpeed = invadersRocketSpeedDefault   # Скорость ракеты. Больше - быстрей

# Загружаем текстуры боевой ракеты (Изменяется лишь пламя из сопла)
rocketFiles = ["rocket01.png", "rocket02.png", "rocket03.png", "rocket04.png"]
rocketTexture = []
for fileName in rocketFiles:
    rocketTexture.append(PhotoImage(file=f"image/rocket/{fileName}"))

rocketObject = None                 # Боевая ракета, которой стреляет игрок: объект на Canvas
rocketSpeedYDefault = 8             # Скорость ракеты по умолчанию
rocketSpeedY = rocketSpeedYDefault  # скорость ракеты по Y
rocketScale = 1.05                  # Коэффициент ускорения выпущенной игроком ракеты

# ======================== ТЕКСТУРЫ ВЗРЫВА ============================
explosionFiles = ["expl01.png", "expl02.png", "expl03.png", "expl04.png",
                  "expl05.png", "expl06.png", "expl07.png", "expl08.png"]
explosionTexture = []
for fileName in explosionFiles:
    explosionTexture.append(PhotoImage(file=f"image/expl/{fileName}"))
level = None   # Текущий уровень игры, задается в globalReset()
frame = 0      # Кадр анимации для инопланетян

# ========================= НАСТРОЙКА ИГРОКА ===========================
score = 0          # Очки игрока
penalty = 0        # Штрафы за промахи
lives = 3          # Жизни
playGame = False   # Игра False - "Нет игры" или True - "Игра началась"
defaltName = "Anonymous"

# ========================= МУНЮ ИГРЫ ===============================

# Кнопка "Старт"
menu1 = Button(root, text="Старт", font=", 20", width=20)
menu1.place(x=-100, y=-100)
menu1["command"] = startGame

# Кнопка "Сброс"
menu2 = Button(root, text="Сброс", font=", 20", width=20)
menu2.place(x=-100, y=-100)
menu2["command"] = restartGame

# Кнопка для продолжения после вывода таблицы рекордов
btnContinueAfterPause = None

# Ниже кнопок расположена таблица рекордов
onMenu = False           # Меню "Выключено"
playerName = None        # Имя игрока
scores = loadScores()    # Список с никами и очками
textScores = None        # Список .create_text для отображения таблицы очков на Canvas

informationLine = None   # "Информационная строка" внизу окна

# ++++++++++++++++++ НАЧИНАЕМ ++++++++++++++++++++++++++++

globalReset()     # Сбрасываем очки и прочее
reset()           # Создаём игровой мир
playGame = True
mainloop()

root.mainloop()



