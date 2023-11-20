import random
import logging
from datetime import datetime

# Настройки логгера
logging.basicConfig(filename='game_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def guess_number():
    # Запись начала игры в лог
    logging.info('Начало игры')
  
    # Получение входных данных от пользователя
    n = int(input("Введите число N: "))
    k = int(input("Введите количество попыток k: "))
  
    # Генерация случайного числа от 1 до N
    secret_number = random.randint(1, n)
  
    attempts = 0
    while attempts < k:
        # Увеличение счетчика попыток
        attempts += 1
      
        # Получение предположения пользователя
        guess = int(input("Введите вашу догадку: "))
      
        # Проверка предположения пользователя
        if guess == secret_number:
            print("Вы угадали!")
            logging.info(f'Игра завершена. Угаданное число: {guess}')
            return
        elif guess < secret_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
      
        # Запись попытки пользователя в лог
        logging.info(f'Попытка {attempts}: {guess}')
    
    # Запись окончания игры в лог
    logging.info(f'Попытки закончились. Загаданное число: {secret_number}')
    print("Попытки закончились")

# Вызов основной функции
guess_number()
