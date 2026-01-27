import random
import os
import time

display = ""

index = 0

czas = 5

print("SNAKE.PY")

print("-----* {🐍} *-----")

print("Wybierz poziom: ")

print("1) Łatwy%newline%2) Średni%newline% 3) Trudny\n")

poziom = input("Wprowadz poziom <1| 2| 3|>: ").lower()

if poziom == "1" or "2" or "3":
    if poziom == "1":
        display = "łatwy"

    if poziom == "2":
        display = "Średni"

    if poziom == "3":
        display = "Trudny"

    print("Wybrano poziom", display)
    time.sleep(1)

for i in range(5):
    if index == 1:
        print(f"Trwa ładowanie... -", end="\r" )
        index = 0
        time.sleep(0.5)
    if index == 0:
        print(f"Trwa ładowanie... |", end="\r" )
        index = 1
        time.sleep(0.5)
    time.sleep(0.5)

print("Załadowano zaczynamy za!", czas)

for i in range(5):
    czas = 5 - i
    print("Gra rozpocznie się za:", czas, "sek", end="\r")
    time.sleep(1)
    if czas == 0:
        break

pkt = 0


WIDTH = 20
HEIGHT = 10

snake = [(5, 5), (5, 4), (5, 3)]
direction = "d"

food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
superfood = (random.randint(0, round((HEIGHT - 1) / 2)), random.randint(0, round((WIDTH - 1) / 2)))


def color_text(text, color = "RED"):
    """
    Takes text as string, and color as string, returns colored text, can be used in terminal
    """
    # BLUE = '\033[94m'
    # CYAN = '\033[96m'
    # GREEN = '\033[92m'
    # ORANGE = '\033[93m'
    # RED = '\033[91m'
    if color == "RED":
        return '\033[91m'+text+'\033[0m'
    elif color == "CYAN":
        return '/033[96m[91m'+text+'\033[0m'
    elif color == "GREEN":
        return '\033[92m'+text+'\033[0m'
    elif color == "ORANGE":
        return '\033[93m'+text+'\033[0m'

def render_board(HEIGHT = HEIGHT, WIDTH = WIDTH):
    print("Twoje punkty:", pkt)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (y, x) == food:
                print(color_text("@"), end="")
            elif (y, x) in snake:
                print(color_text("#", "RED"))
                if (y, x) in snake[0]:
                    print("^", "GREEN")
            elif (y, x) == superfood and food not in superfood:
                print(color_text("%", "ORANGE"), end="")
                continue
            else:
                print(" ", end="")
        print()

def draw():
    os.system("cls" if os.name == "nt" else "clear")
    render_board()
    
#    for y in range (HEIGHT):
#        for x in range (WIDTH):
#            if (y, x) == food:
#                print(color_text("*"), end="")
#            elif (y, x) in snake:
#                print("#", end="")

def getsuperfood(food, proc):
    randomowa = random.randint(1, 100)
    if randomowa <= proc:
        return food
    else:
        pass


while True:
    draw()
    print("Sterowanie: w/s/a/d + Enter")

    move = input("Ruch: ").lower()
    if move in ["w", "s", "a", "d"]:
        direction = move

    head_y, head_x = snake[0]

    if direction == 'w':
        head_y -= 1
    if direction == 's':
        head_y += 1
    if direction == 'a':
        head_x += 1
    if direction == 'd':
        head_x -= 1
    
    print()

    new_head = (head_y, head_x)

    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        draw()
        print("Game Over!")
        break

    snake.insert(0, new_head)


    if new_head == food:
        food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
        pkt += 2
    elif new_head == superfood:
        getsuperfood(superfood, 10)
        pkt += 3
    else:
        snake.pop()

    time.sleep(0.1)
