import random

class MazeGame:
    def __init__(self):
        """Инициализация игры"""
        self.turns_count = {'a': 0, 'w': 0, 'd': 0}
        self.exit_found = False
        self.exit_probability = 0.1
        
    def get_valid_input(self):
        """Получение корректного ввода от пользователя"""
        while True:
            user_input = input("Куда идти? ").lower().strip()
            if user_input in ['a', 'w', 'd']:
                return user_input
            else:
                print("Ошибка! Используйте только [a], [w] или [d]")
    
    def check_exit(self):
        """Проверка, найден ли выход (вероятность 1 к 10)"""
        return random.random() < self.exit_probability
    
    def process_move(self, move):
        """Обработка хода игрока"""
        self.turns_count[move] += 1

        messages = {
            'a': "Повернул налево.",
            'w': "Пошёл прямо.",
            'd': "Повернул направо."
        }

        if self.check_exit():
            self.exit_found = True
            return f"{messages[move]} Выход найден. Ты выиграл."
        else:
            return f"{messages[move]} Выхода пока нет..."
    
    def get_statistics(self):
        """Получение статистики игры"""
        total_moves = sum(self.turns_count.values())
        stats = (
            f"\nДля того, чтобы найти выход ты:\n"
            f"  - {self.turns_count['a']} раз повернул налево\n"
            f"  - {self.turns_count['w']} раз пошёл прямо\n"
            f"  - {self.turns_count['d']} раз повернул направо\n"
            f"Всего ходов: {total_moves}"
        )
        return stats
    
    def play(self):
        """Основной игровой цикл"""
        print("=" * 50)
        print("НАЧИНАЕМ ИГРУ 'ЛАБИРИНТ'")
        print("=" * 50)
        print("Повороты: [a]-Налево, [w]-Прямо, [d]-Направо")
        print("-" * 50)
        
        while not self.exit_found:
            move = self.get_valid_input()

            result = self.process_move(move)
            print(result)

            if self.exit_found:
                print(self.get_statistics())
                print("=" * 50)
                print("ИГРА ОКОНЧЕНА")
                break

if __name__ == "__main__":
    game = MazeGame()
    game.play()