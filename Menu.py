from Labyrinth import (
    Labyrinth
)
from Player import (
    Player
)


class Menu:
    '''Класс для меню.'''

    def __init__(self, player, labyrinth) -> None:
        '''Инициализация класса Menu.

        Создает экземпляры классов Player и Labyrinth.'''

        self.player = player
        self.labyrinth = labyrinth
        
    def display_menu(self) -> None:
        '''Функция для отображения меню.'''

        print("=======================================")
        print("          ИГРА: ЛАБИРИНТ")
        print("=======================================")
        print("1. Начать игру")
        print("2. Статистика")
        print("3. Выход")
        print("=======================================")

    def main(self) -> None:
        '''Основная функция класса Menu.

        Отсюда пользователь выбирает необходимую
        ему опцию, от нее вызывается функция.
        Функция работает до тех пор, пока flag = 1.'''

        flag = 1

        while flag:
            self.display_menu()
            choice = input("Выберите опцию (1-3): ")

            if choice == '1':
                self.player.clear_terminal()

                if self.player.labyrinth_quantity == 0:
                    self.player.gaming(3,3)
                elif self.player.labyrinth_quantity == 1:
                    self.player.gaming(4,4)
                elif self.player.labyrinth_quantity == 2:
                    self.player.gaming(5,5)
                else:
                    print('Вы прошли все уровни! Спасибо за игру')

                    flag = 0
            elif choice == '2':
                self.player.clear_terminal()

                print("Ваша статистика:")
                print(self.player.show_statistic())
            elif choice == '3':
                self.player.clear_terminal()

                print("Выход из игры. Спасибо за игру!")

                flag = 0
            else:
                self.player.clear_terminal()

                print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 4.")


if __name__ == "__main__":
    labyrinth = Labyrinth()
    player = Player(labyrinth)
    menu = Menu(player, labyrinth)

    menu.main()
