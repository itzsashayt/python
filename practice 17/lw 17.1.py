import random
import time
import sys

class FigurePuzzle:
    def __init__(self):
        """Инициализация игры с элементами фигур"""

        self.figures = {
            1: {  
                'name': "Ромб",
                'target': [
                    "  ◇  ",
                    " ◇◇◇ ",
                    "◇◇◇◇◇",
                    " ◇◇◇ ",
                    "  ◇  "
                ],
                'elements': [
                    ["  ◇  ", "  ◇  ", "  ◇  ", "  ◇  ", "  ◇  "],  
                    ["  /  ", " /   ", "/    ", " \\   ", "  \\  "],  
                    ["  \\  ", "   \\ ", "    \\", "   / ", "  /  "],  
                    ["  ◇  ", " ◇◇  ", "◇◇◇  ", " ◇◇  ", "  ◇  "] 
                ]
            },
            2: { 
                'name': "Крест",
                'target': [
                    "  +  ",
                    "  +  ",
                    "+++++",
                    "  +  ",
                    "  +  "
                ],
                'elements': [
                    ["  |  ", "  |  ", "  |  ", "  |  ", "  |  "],
                    ["  -  ", "  -  ", "  -  ", "  -  ", "  -  "],
                    ["  +  ", "  +  ", "  +  ", "  +  ", "  +  "],
                    [" \\   ", "  \\  ", "   \\ ", "  /  ", " /   "]
                ]
            }
        }
        
        self.current_figure = None
        self.current_elements = []
        self.selected_figure_num = 0
    
    def loading_simulation(self):
        """Функция загрузки от 1% до 100%"""
        print("Загрузка игры...")
        for i in range(1, 101):
            time.sleep(0.02)
            progress = "[" + "=" * (i//2) + " " * (50 - i//2) + "]"
            sys.stdout.write(f"\r{progress} {i}%")
            sys.stdout.flush()
        print("\nЗагрузка завершена!\n")
    
    def select_random_figure(self):
        """Случайный выбор одной из двух фигур"""
        self.selected_figure_num = random.randint(1, 2)
        self.current_figure = self.figures[self.selected_figure_num]
        return self.selected_figure_num
    
    def generate_random_elements(self):
        """Генерация случайных элементов для выбранной фигуры"""
        self.current_elements = []
        for i in range(4):
            element_variants = self.get_element_variants(i)
            self.current_elements.append(random.choice(element_variants))
        return self.current_elements
    
    def get_element_variants(self, element_index):
        """Возвращает варианты для каждого элемента"""
        base = self.current_figure['elements'][element_index]

        variants = [base]
        
        if element_index == 0:
            variants.append(["  |  ", "  |  ", "  |  ", "  |  ", "  |  "])
            variants.append(["  :  ", "  :  ", "  :  ", "  :  ", "  :  "])
        elif element_index == 1:
            variants.append(["  -  ", "  -  ", "  -  ", "  -  ", "  -  "])
            variants.append(["  =  ", "  =  ", "  =  ", "  =  ", "  =  "])
        elif element_index == 2:
            variants.append(["  +  ", "  +  ", "  +  ", "  +  ", "  +  "])
            variants.append(["  *  ", "  *  ", "  *  ", "  *  ", "  *  "])
        elif element_index == 3:
            variants.append([" /   ", "  /  ", "   / ", "  \\  ", " \\   "])
            variants.append([" \\   ", "  \\  ", "   \\ ", "  /  ", " /   "])
        
        return variants
    
    def display_figure(self, elements, title="Текущая фигура:"):
        """Отображение фигуры из 4 элементов"""
        print(f"\n{title}")
        print("═" * 30)

        for row in range(5):
            line = ""
            for elem_idx in range(4):
                if elem_idx < len(elements):
                    line += elements[elem_idx][row] + "   "
            print(line)
        print("═" * 30)
    
    def display_target(self):
        """Отображение целевой фигуры"""
        print(f"\nЦЕЛЕВАЯ ФИГУРА: {self.current_figure['name']}")
        print("═" * 30)
        for line in self.current_figure['target']:
            print(line)
        print("═" * 30)
    
    def replace_element(self, element_num):
        """Замена выбранного элемента"""
        if 1 <= element_num <= 4:
            element_index = element_num - 1
            variants = self.get_element_variants(element_index)

            current_variant = self.current_elements[element_index]
            available_variants = [v for v in variants if v != current_variant]
            
            if available_variants:
                self.current_elements[element_index] = random.choice(available_variants)
                print(f"Элемент {element_num} изменён!")
            else:
                self.current_elements[element_index] = random.choice(variants)
                print(f"Элемент {element_num} изменён!")
            
            return True
        else:
            print("Ошибка! Введите число от 1 до 4")
            return False
    
    def check_solution(self):
        """Проверка, собрана ли правильная фигура"""
        assembled = []
        for row in range(5):
            line = ""
            for elem_idx in range(4):
                if elem_idx < len(self.current_elements):
                    line += self.current_elements[elem_idx][row][2]
            assembled.append(line)
        target_center = []
        for line in self.current_figure['target']:
            target_center.append(line.replace(" ", ""))
        
        assembled_center = []
        for line in assembled:
            assembled_center.append(line.replace(" ", ""))
        
        return assembled_center == target_center
    
    def get_user_input(self):
        """Получение ввода от пользователя"""
        while True:
            try:
                print("\nВыберите элемент для изменения (1-4):")
                print("Или введите 0 для выхода")
                choice = input("Ваш выбор: ").strip()
                
                if choice == '0':
                    return 0
                
                choice_num = int(choice)
                if 1 <= choice_num <= 4:
                    return choice_num
                else:
                    print("Пожалуйста, введите число от 1 до 4")
            except ValueError:
                print("Пожалуйста, введите число!")
    
    def play(self):
        """Основной игровой цикл"""
        self.loading_simulation()

        figure_num = self.select_random_figure()
        print(f"Вам выпала Фигура {figure_num}: {self.current_figure['name']}")

        self.display_target()

        self.generate_random_elements()
        
        moves = 0

        while True:
            moves += 1

            self.display_figure(self.current_elements, f"Ход {moves}:")

            if self.check_solution():
                print("\n" + "=" * 40)
                print("ПОЗДРАВЛЯЕМ! Вы собрали фигуру!")
                print(f"Фигура: {self.current_figure['name']}")
                print(f"Количество ходов: {moves}")
                print("=" * 40)
                break

            choice = self.get_user_input()
            
            if choice == 0:
                print("Игра завершена.")
                break

            self.replace_element(choice)
    
    def show_instructions(self):
        """Показать инструкцию"""
        print("=" * 50)
        print("ИГРА: СОБЕРИ ФИГУРУ")
        print("=" * 50)
        print("Инструкция:")
        print("1. Вам показывают, какая фигура должна получиться")
        print("2. Фигура состоит из 4 элементов (пронумерованы 1-4)")
        print("3. Вводите цифру 1-4, чтобы изменить соответствующий элемент")
        print("4. Элементы будут меняться случайным образом")
        print("5. Цель - собрать фигуру, идентичную целевой")
        print("=" * 50)

if __name__ == "__main__":
    game = FigurePuzzle()
    game.show_instructions()
    game.play()