# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие —1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты -3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

COMISSION: float = 0.015
LOWER_LIMIT: int = 30
UPPER_LIMIT: int = 600
RATE: float = 0.03
RICH: int = 5000000
NALOG: float = 0.1

ballans: float= 0
counter: int = 0

while True:
    print('Сумма на счёте:', ballans)
    print('Для поплнения введите положительную сумму кратную 50.')
    print('Для снятия введите отрицательную сумму кратную 50.')
    print('Для выхода введите ноль.')
    sum: int = int(input('Сумма = '))
    if sum == 0:
        break
    if ballans > RICH:
        ballans -= round(ballans * NALOG, 2)
    if sum % 50 != 0:
        print('Введённая сумма не кратна 50 - операция отменена.')
        continue
    elif sum < 0:
        if abs(sum) <= ballans:
            percent: float = round(sum * COMISSION, 2)
            if percent in range(LOWER_LIMIT, UPPER_LIMIT):
                ballans -= percent
            elif percent <= LOWER_LIMIT:
                ballans -= LOWER_LIMIT
            elif percent >= UPPER_LIMIT:
                ballans -= UPPER_LIMIT
            ballans += sum
        else:
            print('Введённая сумма снятия больше остатка на счёте - операция отменена.')
            continue
    elif sum > 0:
        ballans += sum
    counter =+1
    if counter % 3 == 0:
        ballans -= round(ballans * RATE, 2)
