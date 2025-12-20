import os


class Player:
    '''Класс для игрока.'''

    def __init__(self, labyrinth_ekz, labyrinth_quantity: int=0) -> None:
        '''Конструктор для Player.
        
        Args:
            labyrinth_ekz: Экземпляр класса лабиринт.
            labyrinth_quantity: Кол-во пройденных лабиринтов.
        '''

        self.labyrinth = labyrinth_ekz
        self.labyrinth_quantity = labyrinth_quantity

    def play(self, matrix: list, start_point: tuple, final_point: tuple):
        '''Функция для перемещения.
        
        Args: 
            matrix: Лабиринт в виде матрицы.
            start_point: Текущая точка.
            final_point: Конечная точка.
            
        Returns:
            str: Игра окончена.
            matrix: Лабиринт в виде матрицы.
            new_conceptual_start_point: Новая текущая точка.
            final_point: Конечная точка.
        '''
  
        sx = start_point[0]
        sy = start_point[1]
        fx = final_point[0]
        fy = final_point[1]
    
        if matrix[fx][fy] == 2:
            self.labyrinth_quantity += 1

            return "Игра окончена"

        self.labyrinth.draw_labyrinth(matrix, (sx, sy), (fx, fy))

        moving = input()
    
        new_conceptual_start_point = (sx,sy)
    
        match moving:
            case 'R':
                if (sy + 1 < len(matrix[0]) and
                    matrix[sx][sy + 1] == 1):
                        matrix[sx][sy + 1] = 2      
                        matrix[sx][sy] = 1
                        new_conceptual_start_point = (sx, sy + 1)
                
            case 'L':
                if (sy - 1 >= 0 and
                    matrix[sx][sy - 1] == 1):
                        matrix[sx][sy - 1] = 2
                        matrix[sx][sy] = 1
                        new_conceptual_start_point = (sx, sy - 1)

            case 'U':
                if (sx - 1 >= 0 and
                    matrix[sx - 1][sy] == 1):
                        matrix[sx - 1][sy] = 2
                        matrix[sx][sy] = 1
                        new_conceptual_start_point = (sx - 1, sy)

            case 'D':
                if (sx + 1 < len(matrix) and
                    matrix[sx + 1][sy] == 1):
                        matrix[sx + 1][sy] = 2
                        matrix[sx][sy] = 1
                        new_conceptual_start_point = (sx + 1, sy)

        return matrix, new_conceptual_start_point, final_point
    
    def gaming(self, dx: int, dy: int) -> None:
        '''Функция для игры. Генерируется лабиринт, игра продолжается
        до тех пор, пока кол-во пройденных лабиринтов не увеличится.
        
        Args:
            dx: Высота матрицы достижений.
            dy: Ширина матрицы достижений.
        '''

        real_matrix, start_point, final_point = self.labyrinth.generating_labyrinth(dx, dy)
        sx, sy = start_point[0]*2+1, start_point[1]*2+1
        fx, fy = final_point[0]*2+1, final_point[1]*2+1

        real_matrix = self.labyrinth.from_real_matrix_to_labyrinth(real_matrix)

        current_labyrinth_quantity = self.labyrinth_quantity

        while self.labyrinth_quantity == current_labyrinth_quantity:
            self.clear_terminal_labyrinth()
            real_matrix, (sx, sy), (fx, fy) = self.play(real_matrix, (sx, sy), (fx, fy))

            if sx+1 == fx+1 and fy+1 == sy+1:
                self.labyrinth_quantity +=1
                self.labyrinth.difficulty += 1
    
    def clear_terminal_labyrinth(self) -> None:
        '''Функция для чистки терминала
        во время игры.'''

        os.system('cls' if os.name == 'nt' else 'clear')

        print('----------------------------------------------------')
        print('                      ЛАБИРИНТ ')
        print(f'                 Сложность: {self.labyrinth.display_difficulty()}')
        print('----------------------------------------------------')

    def clear_terminal(self) -> None:
        '''Функция для чистки терминала
        в меню.'''

        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_statistic(self) -> str:
        '''Класс для показа статистики.
        
        Returns: 
            labyrinth_quantity: Количество пройденных лабиринтов.
        '''

        return f" Количество пройденных лабиринтов: {self.labyrinth_quantity}"
