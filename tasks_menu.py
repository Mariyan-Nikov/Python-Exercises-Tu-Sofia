import random

def task_1_discount():
    try:
        age = int(input("Въведете Вашата възраст (age): "))
        if 18 <= age <= 26:
            print("Имате право на студентска отстъпка.")
        else:
            print("Нямате право на студентска отстъпка.")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число за възраст.")

def task_2_divisible_by_3():
    try:
        number = int(input("Въведете цяло число: "))
        if number % 3 == 0:
            print(f"Числото {number} е делимо на 3.")
        else:
            print(f"Числото {number} не е делимо на 3.")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_3_language_level():
    try:
        points = int(input("Въведете броя на точките: "))
        level = ""
        if points >= 90:
            level = "C1"
        elif points >= 75:
            level = "B2"
        elif points >= 60:
            level = "B1"
        elif points >= 45:
            level = "A2"
        else:
            level = "A1"

        print(f"При {points} точки, Вашето ниво на езиково владеене е: {level}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число за точки.")

def task_4_odd_numbers():
    print("Нечетните числа от 1 до 30 са:")
    odd_numbers = []
    for i in range(1, 31):
        if i % 2 != 0:
            odd_numbers.append(i)
    print(*odd_numbers, sep=", ")

def task_5_sum_even():
    try:
        n = int(input("Въведете цяло число n: "))
        if n < 2:
            print("Няма четни числа в интервала [2, n]. Сумата е 0.")
            return

        sum_even = 0
        for i in range(2, n + 1, 2):
            sum_even += i

        print(f"Сумата на всички четни числа от 2 до {n} е: {sum_even}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_6_multiplication_table_7():
    print("Таблица за умножение по 7 (от 1 до 10):")
    result_parts = []
    for i in range(1, 11):
        product = 7 * i
        result_parts.append(f"7 x {i} = {product}")
    print(*result_parts, sep=", ")

def task_7_even_divisors():
    try:
        number = int(input("Въведете цяло число: "))
        if number <= 0:
            print("Моля, въведете положително цяло число.")
            return

        even_divisors = []
        for i in range(1, number + 1):
            if number % i == 0 and i % 2 == 0:
                even_divisors.append(i)

        if even_divisors:
            print(f"Четните делители на числото {number} са: {even_divisors}")
        else:
            print(f"Числото {number} няма четни делители.")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_8_count_zeros():
    try:
        number_str = input("Въведете цяло число: ")
        count_zeros = number_str.count('0')

        print(f"Броят на нулите в числото е: {count_zeros}")
    except Exception:
        print("Възникна грешка при обработката на входа.")

def task_9_skip_multiples_of_4():
    print("Числата от 1 до 30, като се пропускат кратните на 4, са:")
    result_numbers = []
    for i in range(1, 31):
        if i % 4 == 0:
            continue
        result_numbers.append(i)
    print(*result_numbers, sep=", ")

def task_10_first_multiple_of_7():
    try:
        start = int(input("Въведете начало на интервала (start): "))
        end = int(input("Въведете край на интервала (end): "))

        if start >= end:
            print("Началото на интервала трябва да е по-малко от края.")
            return

        first_multiple = None
        for i in range(start + 1, end):
            if i % 7 == 0:
                first_multiple = i
                break

        if first_multiple is not None:
            print(f"Първото число, кратно на 7, в интервала ({start}, {end}) е: {first_multiple}")
        else:
            print(f"В интервала ({start}, {end}) няма число, кратно на 7.")

    except ValueError:
        print("Невалиден вход. Моля, въведете цели числа за начало и край.")

def task_1_separate_digits():
    try:
        number_str = input("Въведете цяло число: ")
        even_digits = []
        odd_digits = []

        for digit_char in number_str:
            digit = int(digit_char)
            if digit % 2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)

        print(f"Четните цифри на числото са: {even_digits}")
        print(f"Нечетните цифри на числото са: {odd_digits}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_2_above_average():
    try:
        count = int(input("Въведете брой на случайните числа за първия списък: "))
        if count <= 0:
            print("Броят трябва да е положителен.")
            return

        random_list = [random.randint(1, 100) for _ in range(count)]
        print(f"Първият списък от случайни числа е: {random_list}")

        average = sum(random_list) / count
        print(f"Средната стойност на числата е: {average:.2f}")

        above_average_list = [num for num in random_list if num > average]

        print(f"Новият списък (числа > средното) е: {above_average_list}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_3_word_count():
    text = input("Въведете текст: ")

    import re
    words = re.findall(r'\b\w+\b', text.lower())

    word_count = len(words)

    distinct_word_count = len(set(words))

    print(f"Общ брой на думите в текста: {word_count}")
    print(f"Брой на различните думи в текста: {distinct_word_count}")

def task_4_squares_dict_1_to_10():
    squares_dict = {i: i**2 for i in range(1, 11)}

    print("Речник (число: квадрат):")
    print(squares_dict)

def task_5_repeated_chars():
    input_string = input("Въведете низ (текст): ")
    
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    
    print(f"Символи, които се срещат повече от веднъж: {repeated_chars}")

def task_6_product_of_neighbors():
    try:
        count = int(input("Въведете брой на случайните числа за първия списък (поне 2): "))
        if count < 2:
            print("Броят трябва да е поне 2.")
            return

        random_list = [random.randint(1, 10) for _ in range(count)]
        print(f"Първият списък е: {random_list}")

        new_list = []
        for i in range(len(random_list) - 1):
            product = random_list[i] * random_list[i+1]
            new_list.append(product)

        print(f"Новият списък (произведение на съседи) е: {new_list}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_7_cubes_dict():
    try:
        n = int(input("Въведете цяло число n: "))
        if n <= 0:
            print("Моля, въведете положително цяло число.")
            return

        cubes_dict = {i: i**3 for i in range(1, n + 1)}

        print(f"Речник (число: куб) за числата от 1 до {n}:")
        print(cubes_dict)
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_8_remove_duplicates():
    try:
        count = int(input("Въведете брой на случайните числа за първия списък: "))
        if count <= 0:
            print("Броят трябва да е положителен.")
            return

        random_list = [random.randint(1, 7) for _ in range(count)]
        print(f"Първият списък е: {random_list}")

        unique_list = list(set(random_list))

        print(f"Списък без повтарящи се елементи: {unique_list}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_9_char_position_dict():
    word = input("Въведете дума: ")
    
    position_dict = {}
    for index, char in enumerate(word):
        if char not in position_dict:
            position_dict[char] = index + 1

    print(f"Речник (буква: първа позиция): {position_dict}")

def task_10_even_odd_dict():
    numbers = range(1, 21)

    even_odd_dict = {
        num: "четно" if num % 2 == 0 else "нечетно"
        for num in numbers
    }

    print("Речник (число: четно/нечетно):")
    print(even_odd_dict)

def task_11_divisors_tuple():
    try:
        number = int(input("Въведете цяло число: "))
        if number <= 0:
            print("Моля, въведете положително цяло число.")
            return

        divisors_list = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors_list.append(i)

        divisors_tuple_original = tuple(divisors_list)
        
        divisors_list.sort(reverse=True)
        divisors_tuple_descending = tuple(divisors_list)

        print(f"Кортеж с всички делители: {divisors_tuple_original}")
        print(f"Кортеж с делителите в намаляващ ред: {divisors_tuple_descending}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_12_insert_zeros_ones():
    try:
        count = int(input("Въведете брой на случайните цели числа: "))
        if count <= 0:
            print("Броят трябва да е положителен.")
            return

        random_list = [random.randint(1, 10) for _ in range(count)]
        print(f"Първият списък е: {random_list}")

        if count <= 1:
            print("Няма съседни елементи за сравнение.")
            return

        new_list = []
        for i in range(len(random_list) - 1):
            num1 = random_list[i]
            num2 = random_list[i+1]
            sum_neighbors = num1 + num2
            
            new_list.append(num1)

            if sum_neighbors % 2 == 0:
                new_list.append(0)
            else:
                new_list.append(1)

        new_list.append(random_list[-1])

        print(f"Новият списък с вмъкнати 0/1 е: {new_list}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_13_word_length_dict():
    text = input("Въведете текст: ")

    import re
    words = re.findall(r'\b\w+\b', text)
    
    word_length_dict = {word: len(word) for word in words}

    print("Речник (дума: дължина):")
    print(word_length_dict)

def task_14_multiples_of_3_or_5():
    try:
        n = int(input("Въведете цяло число n: "))
        if n <= 0:
            print("Моля, въведете положително цяло число.")
            return

        full_list = list(range(1, n + 1))
        print(f"Списъкът от 1 до {n} е: {full_list}")

        multiples_list = [num for num in full_list if num % 3 == 0 or num % 5 == 0]

        print(f"Новият списък (кратни на 3 или 5) е: {multiples_list}")
    except ValueError:
        print("Невалиден вход. Моля, въведете цяло число.")

def task_15_palindrome_check():
    phrase = input("Въведете дума или фраза: ")
    
    processed_text = phrase.lower().replace(" ", "")

    is_palindrome = processed_text == processed_text[::-1]

    if is_palindrome:
        print("Да")
    else:
        print("Не")

def run_menu():
    tasks = {
        1: ("Студентска отстъпка (18-26г.)", task_1_discount),
        2: ("Число, делимо на 3", task_2_divisible_by_3),
        3: ("Ниво на езиково владеене (elif)", task_3_language_level),
        4: ("Нечетни числа от 1 до 30", task_4_odd_numbers),
        5: ("Сума на четните числа от 2 до n", task_5_sum_even),
        6: ("Таблица за умножение по 7", task_6_multiplication_table_7),
        7: ("Четни делители на число", task_7_even_divisors),
        8: ("Брой на цифрите 0 в число", task_8_count_zeros),
        9: ("Числа от 1 до 30 (пропуска кратни на 4)", task_9_skip_multiples_of_4),
        10: ("Първо число, кратно на 7, в интервал (start, end)", task_10_first_multiple_of_7),
        
        11: ("Разделяне на четни/нечетни цифри", task_1_separate_digits),
        12: ("Числа по-големи от средното", task_2_above_average),
        13: ("Брой на думите и различни думи", task_3_word_count),
        14: ("Речник: 1-10 и техните квадрати", task_4_squares_dict_1_to_10),
        15: ("Повтарящи се символи в низ", task_5_repeated_chars),
        16: ("Произведение на съседни елементи", task_6_product_of_neighbors),
        17: ("Речник: 1-n и техните кубове", task_7_cubes_dict),
        18: ("Премахване на повтарящи се елементи", task_8_remove_duplicates),
        19: ("Речник: буква и първа позиция", task_9_char_position_dict),
        20: ("Речник: 1-20, четно/нечетно", task_10_even_odd_dict),
        21: ("Кортежи с делители (намаляващ ред)", task_11_divisors_tuple),
        22: ("Вмъкване на 0/1 между съседни числа", task_12_insert_zeros_ones),
        23: ("Речник: дума и нейната дължина", task_13_word_length_dict),
        24: ("Кратни на 3 или 5 от 1 до n", task_14_multiples_of_3_or_5),
        25: ("Проверка за палиндром", task_15_palindrome_check)
    }

    while True:
        print("\n" + "="*50)
        print(">>> МЕНЮ ЗА ИЗБОР НА ЗАДАЧА <<<")
        print("="*50)
        
        print("\n--- Задачи с Условни Оператори и Цикли (1-10) ---")
        for i in range(1, 11):
            print(f"[{i:02d}] {tasks[i][0]}")

        print("\n--- Задачи със Списъци, Речници и Кортежи (1-15) ---")
        for i in range(11, 26):
            print(f"[{i}] {tasks[i][0]}")
            
        print("\n[00] Изход")
        print("-" * 50)
        
        try:
            choice = input("Въведете номера на задачата (1-25) или 0 за изход: ")
            choice = int(choice)
            
            if choice == 0:
                print("Програмата приключи. Довиждане!")
                break
            elif 1 <= choice <= 25:
                print(f"\n--- ИЗПЪЛНЕНИЕ НА ЗАДАЧА {choice}: {tasks[choice][0]} ---")
                tasks[choice][1]() 
                print("\n" + "--- КРАЙ НА ЗАДАЧА ---")
                input("\nНатиснете Enter за да се върнете в менюто...")
            else:
                print("Невалиден избор. Моля, въведете число от 0 до 25.")
        except ValueError:
            print("Невалиден вход. Моля, въведете цяло число.")
        except Exception as e:
            print(f"Възникна неочаквана грешка: {e}")

if __name__ == "__main__":
    run_menu()