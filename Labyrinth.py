import random


class Labyrinth:
    '''Класс для лабиринта.'''

    def __init__(self, height: int=3, width: int=3, difficulty: int=1) -> None: 
        '''Конструктор для лабиринта.
        
        Args:
            height: Высота матрицы достижений.
            width: Ширина матрицы достижений.
            difficulty: Сложность.
        '''

        self.height = height
        self.width = width
        self.difficulty = difficulty
    
    def display_difficulty(self) -> str:
        '''Функция для отображения сложности текущего лабиринта.
        
        Returns:
            str: Легкая, Средняя, Тяжелая.'''
        
        if self.difficulty == 1:

            return 'Легкая'
        elif self.difficulty == 2:

            return 'Средняя'
        elif self.difficulty == 3:

            return 'Тяжелая'

    def start_point_generation(self, x:int, y:int) -> tuple:
        '''Генерация стартовой точки.
        
        Args:
            x: Высота матрицы достижений.
            y: Ширина матрицы достижений.
            
        Returns:
            start_point: Стартовая тчока.
        '''

        if random.choice([True, False]):
            if random.choice([True, False]):
                start_point = (0, random.randint(1, y-2))
            else:
                start_point = (x-1, random.randint(1, y-2))
        else:
            if random.choice([True, False]):
                start_point = (random.randint(1, x-2), 0)
            else:
                start_point = (random.randint(1, x-2), y-1)

        return start_point
    
    def final_point_generation(self, x: int, y: int, start_point: tuple) -> tuple:
        '''Функция для генерация финальной точки.
        
        Args:
            x: Высота матрицы достижений.
            y: Ширина матрицы достижений.
            start_point: Стартовая точка.

        Returns:
            okaym: Рандомная точка из списка точек окаймляющих матрицу достижения.
        '''

        okaym_points = []

        for i in range(1, x-1):
            if (0, i) != start_point:
                okaym_points.append((0, i))

            if (x-1, i) != start_point:
                okaym_points.append((x-1, i))

        for i in range(1, y-1):
            if (i, x-1) != start_point:
                okaym_points.append((i, x-1))

            if (i, 0) != start_point:
                okaym_points.append((i, 0))
        
        okaym = random.choice(okaym_points)

        return okaym
    
    def choice(self, matrix: list, x: int, y: int, dx: int, dy: int)-> list:
        '''Функция для выбора пути.

        Args:
            matrix: Матрица достижения.
            x: Координата по высоте текущей точки матрицы достижений.
            y: Координата по ширине текущей точки матрицы достижений.
            dx: Высота матрицы достижений.
            dy: Ширина матрицы достижений.
        
        Returns:
            choices_list: Список из возможных вариантов ходов.
            int: -1.
        '''

        choices_list = []
        if x < dx-1 and matrix[x+1][y] == 0:
            choices_list.append((x+1,y, 1, 0))
        elif x > 0 and matrix[x-1][y] == 0:
            choices_list.append((x-1,y, -1, 0))
        elif y < dy-1 and matrix[x][y+1] == 0:
            choices_list.append((x,y+1, 0, 1))
        elif y> 0 and matrix[x][y-1] == 0:
            choices_list.append((x,y-1, 0, -1))
        else:

            return -1
        
        return choices_list

    def generating_labyrinth(self, x: int, y: int):
        '''Функция для генерации лабиринта.

        Args:
            x: Высота матрицы достижений.
            y: Ширина матрицы достижений.

        Returns:
            real_matrix: Матрица переходов.
            start_point: Стартовая точка.
            final_point: Конечная точка.
        '''

        matrix = [[0 for _ in range(y)] for _ in range(x)]
        start_point = self.start_point_generation(x,y)
        final_point = self.final_point_generation(x,y,start_point)

        real_matrix = [[0 for _ in range(2*y-1)] for _ in range(2*x-1)]

        for i in range(2*x-1):
            for j in range(2*y-1):
                if i % 2 == 0 and j % 2 == 0:
                    real_matrix[i][j] = 1

        p = 1
        matrix[start_point[0]][start_point[1]] = 1

        step_history = [start_point]
        dx,dy = start_point
        step = self.choice(matrix,dx,dy,x,y)

        while p < x*y:
            if step != -1:
                new_step = random.choice(step)
                nx, ny, dx, dy = new_step
                matrix[nx][ny] = 1
                step_history.append((nx, ny))
                
                if dx == 1:
                    real_matrix[2*nx-1][2*ny] = 1
                elif dx == -1:
                    real_matrix[2*nx+1][2*ny] = 1
                elif dy == 1:
                    real_matrix[2*nx][2*ny-1] = 1
                elif dy == -1:
                    real_matrix[2*nx][2*ny+1] = 1

                step = self.choice(matrix, nx, ny, x, y)
                p +=1
            else:
                lx, ly = step_history[-1]
                step_history.pop(-1)
                step = self.choice(matrix, lx, ly, x, y)

        return real_matrix, start_point, final_point
    
    def from_real_matrix_to_labyrinth(self, real_matrix: list) -> list:
        '''Функция для превращения матрицы переходов в матрицу лабиринта.
        
        Args:
            real_matrix: Матрица переходов.
            
        Returns:
            labyrinth: Матрица лабиринта.
        '''

        labyrinth = [[0 for _ in range(len(real_matrix[0])+2)] for _ in range(len(real_matrix)+2)]

        for row in range(1, len(real_matrix)+1):
            for column in range(1, len(real_matrix[0])+1):
                labyrinth[row][column] = real_matrix[row-1][column-1]
        
        return labyrinth
    
    def draw_labyrinth(self, labyrinth: list, start_point: tuple, final_point: tuple) -> None:
        '''Функция для рисования лабиринта.
        
        Args: 
            labyrinth: Матрица в виде лабиринта.
            start_point: Текущая точка.
            final_point: Конечная точка.
        '''

        sx, sy = start_point
        fx, fy = final_point

        if fx == len(labyrinth)-2:
            labyrinth[fx+1][fy] = 1
        elif fy == len(labyrinth[0])-2:
            labyrinth[fx][fy+1] = 1
        elif fx == 1:
            labyrinth[fx-1][fy] = 1
        elif fy == 1:
            labyrinth[fx][fy-1] = 1

        for labyrinth_row in range(len(labyrinth)):
            for labyrinth_column in range(len(labyrinth[0])):
                if labyrinth[labyrinth_row][labyrinth_column] == 0:
                    print('██', end='')
                else:
                    if (labyrinth_row, labyrinth_column) == (sx, sy):
                        print('P ', end='')
                    else:
                        print('  ', end='')
            print('')

        print('U - Вверх', 'D - Вниз')
        print('R - Вправо', 'L - Влево')
