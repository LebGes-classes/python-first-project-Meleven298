import random


class Labyrinth:
    '''Класс для лабиринта.'''

    def __init__(self, height, width):
        '''Конструктор для лабиринта.'''

        self.height = height
        self.width = width

    def start_point_generation(self, x, y):
        '''Генерация стартовой точки.'''

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
    
    def final_point_generation(self, x, y, start_point):
        '''Функция для генерация финальной точки.'''

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
    
    def choice(self, matrix, x, y):
        '''Функция для выбора пути.'''

        choices_list = []
        if x < self.height-1 and matrix[x+1][y] == 0:
            choices_list.append((x+1,y, 1, 0))
        elif x > 0 and matrix[x-1][y] == 0:
            choices_list.append((x-1,y, -1, 0))
        elif y < self.width-1 and matrix[x][y+1] == 0:
            choices_list.append((x,y+1, 0, 1))
        elif y> 0 and matrix[x][y-1] == 0:
            choices_list.append((x,y-1, 0, -1))
        else:
            return -1
        return choices_list

    def generating_labyrinth(self, x, y):
        '''Генерация лабиринта.'''

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
        x,y = start_point
        step = self.choice(matrix,x,y)

        while p < self.height*self.width:
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
                step = self.choice(matrix, nx, ny)
                p +=1

            else:
                lx, ly = step_history[-1]
                step_history.pop(-1)
                step = self.choice(matrix, lx, ly)

        return real_matrix, start_point, final_point
    
    def draw_labyrinth(self, real_matrix, start_point, final_point):
        '''Функция для рисования лабиринта.'''

        sx, sy = start_point
        fx, fy = final_point

        for i in range(len(real_matrix)):
            for j in range(len(real_matrix)):
                print(real_matrix[i][j], '', end='')
            print('')

        labyrinth = [[0 for _ in range(len(real_matrix[0])+2)] for _ in range(len(real_matrix)+2)]

        for row in range(1, len(real_matrix)+1):
            for column in range(1, len(real_matrix[0])+1):
                labyrinth[row][column] = real_matrix[row-1][column-1]

        for labyrinth_row in range(len(labyrinth)):
            for labyrinth_column in range(len(labyrinth[0])):
                if labyrinth[labyrinth_row][labyrinth_column] == 0:
                    print('██', end='')
                else:
                    if (labyrinth_row-1, labyrinth_column-1) == (sx, sy):
                        print('2 ', end='')
                    elif (labyrinth_row-1, labyrinth_column-1) == (fx, fy):
                        print('F ', end='')
                    else:
                        print('  ', end='')
            print('')