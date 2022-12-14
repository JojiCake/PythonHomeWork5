# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# БЛОКИ

# Выбор режима игры (человек-человек / человек-компьютер)
# Инициализация

# Главный цикл

# Интерфейс + ввод
# Логика игры
# Ход
# Логика компьютера


from ast import Pass
import os
import random
import time

def clear(): return os.system('cls')

# Структура с данными об игре
class game:
    candies_on_table = 2021
    candies_to_take = 0
    player1_name = "Игрок 1"
    player2_name = "Игрок 2"
    mode = 1
    turn = 1

    def __init__(self, candies_on_table, candies_to_take, player1_name, player2_name, mode, turn):
        self.candies_on_table = candies_on_table
        self.candies_to_take = candies_to_take
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.mode=mode
        self.turn = turn

# Функция, определяющая чей ход следующий, количество оставшихся конфет и выводящая данные о совершённом ходе
def game_engine(this_game):

    if this_game.turn == 1:
        print(f"Игрок {this_game.player1_name}", end="")
        this_game.turn = 2
    else:
        print(f"Игрок {this_game.player2_name}", end="")
        this_game.turn = 1

    this_game.candies_on_table -= this_game.candies_to_take
    print(f" берёт {this_game.candies_to_take} конфет. На столе остаётся {this_game.candies_on_table} конфет.\n")

    return this_game

# Функция ввода данных нового хода игроком
def player_move(this_game):

    temp_candies_to_take = 0

    if this_game.mode == 1:
        if this_game.turn == 1:
            print(f"Ход {this_game.player1_name}. На столе лежит {this_game.candies_on_table} конфет. Сколько из них вы возьмёте?")
        else:
            print(f"Ход {this_game.player2_name}. На столе лежит {this_game.candies_on_table} конфет. Сколько из них вы возьмёте?")
        while True:
                try:
                    temp_candies_to_take = int(input("Введите количество конфет от 1 до 28 или 0, чтобы выйти: "))
                    if temp_candies_to_take not in range(0, 29):
                        print("Вы можете взять только от 1 до 28 конфет. Повторите попытку.\n")
                        continue
                    if temp_candies_to_take > this_game.candies_on_table:
                        print("Вы не можете взять больше конфет чем лежит на столе. Повторите попытку.\n")
                        continue
                    break
                except ValueError:
                    print("Вы ввели неправильное значение. Попробуйте ещё раз.\n")           
        if temp_candies_to_take > this_game.candies_on_table:
            print("Вы не можете взять больше конфет чем лежит на столе. Повторите попытку.\n")
        elif temp_candies_to_take not in range(0, 29):
            print("Вы можете взять только от 1 до 28 конфет. Повторите попытку.\n")
    elif this_game.mode == 2:
        if this_game.turn == 1:
            print(f"Ход {this_game.player1_name}. На столе лежит {this_game.candies_on_table} конфет. Сколько из них вы возьмёте?")
            while True:
                try:
                    temp_candies_to_take = int(input("Введите количество конфет от 1 до 28 или 0, чтобы выйти: "))
                    if temp_candies_to_take not in range(0, 29):
                        print("Вы можете взять только от 1 до 28 конфет. Повторите попытку.\n")
                        continue
                    if temp_candies_to_take > this_game.candies_on_table:
                        print("Вы не можете взять больше конфет чем лежит на столе. Повторите попытку.\n")
                        continue
                    break
                except ValueError:
                    print("Вы ввели неправильное значение. Попробуйте ещё раз.\n")            
        else:
            temp_candies_to_take = pc_logic(this_game.candies_on_table)
    else:
        if this_game.turn == 1:
            temp_candies_to_take = pc_logic(this_game.candies_on_table)          
        else:
            temp_candies_to_take = pc_logic(this_game.candies_on_table)

    this_game.candies_to_take = temp_candies_to_take
    return this_game

# Логика игры компьютера
def pc_logic(candies_on_table):
    if candies_on_table > 56:
        candies_to_take = random.randint(1, 28)
    elif candies_on_table <= 28:
        candies_to_take = candies_on_table
    else:
        if candies_on_table % 28 == 0:
            candies_to_take = 27
        elif candies_on_table % 28 == 1:
            candies_to_take = random.randint(1, 28)
        else:
            candies_to_take = candies_on_table % 28 - 1
    time.sleep(1)
    return candies_to_take

# Функция инициализации новой игры
def game_init(candies_on_table):
    candies_to_take = 0
    turn=1

    print(f"Добро пожаловать в игру!\n\
Условия простые. На столе лежит {candies_on_table} конфет.\n\
За один ход игрок должен взять не более чем 28 конфет.\n\
Выигрывает тот, кто заберёт со стола последние конфеты\n")                

    print(f"Выберите, кто будет играть?\n 1 - человек vs человек\n 2 - человек vs компьютер\n")

    while True:
        try:
            play_mode = int(input("Введите цифру: "))
            if play_mode not in [1,2,9]:
                print("Вы ввели неправильное значение, попробуйте ещё раз\n")
            else:
                break
        except ValueError:
            print("Вы ввели неправильное значение, попробуйте ещё раз\n")

    print()

    if play_mode==1:
        player1_name = input("Как зовут игрока 1? - ")
        player2_name = input("Как зовут игрока 2? - ")
    elif play_mode==2:
        player1_name = input("Как зовут игрока? - ")
        player2_name = "Компьютер"
    else:
        player1_name = "бот Николай"
        player2_name = "бот Константин"

    clear()

    print("\nЧто ж, бросаем жребий, кто ходит первым\n")
    time.sleep(1)
    if random.randint(1, 2) == 1:
        print(f"{player1_name} ходит первым")
        turn = 1
    else:
        print(f"{player2_name} ходит первым")
        turn = 2

    time.sleep(1)
    print("\nИгра началась\n")

    this_game = game(candies_on_table, candies_to_take, player1_name, player2_name, play_mode, turn)
    return this_game

# Главный цикл игры
def main_loop(candies_on_table):
    this_game = game_init(candies_on_table)

    while True:
        this_game = player_move(this_game)

        if this_game.candies_to_take in range (0,29):
            if this_game.candies_to_take == 0:
                break
            else:
                this_game = game_engine(this_game)

        if this_game.candies_on_table == 0:
            if this_game.turn == 1:
                print(f"Игрок {this_game.player2_name} победил!!!\n")
            else:
                print(f"Игрок {this_game.player1_name} победил!!!\n")
            break
    return 0

# Начало игры

clear()
while True:
    try:
        num_of_candies = int(input("Введите количество конфет: "))
        if num_of_candies < 60:
            print("Слишком мало конфет, чтобы нормально поиграть. Давайте побольше\n")
        elif num_of_candies > 2021:
            print("Слишком много конфет, будем играть всю ночь? Давайте поменьше\n")
        else:
            break
    except ValueError:
        print("Вы ввели неправильное значение, попробуйте ещё раз\n")
clear()
main_loop(num_of_candies)
print("\nGame Over!\n")