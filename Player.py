class Player:
    def __init__(self, labyrinth_ekz):
        self.labyrinth = labyrinth_ekz
        self.labyrinth_quantity = 0

    def play(self, matrix, start_point, final_point):
        '''Функция для игры.'''
  
        sx = start_point[0]
        sy = start_point[1]
        fx = final_point[0]
        fy = final_point[1]
    
        if matrix[fx][fy] == 2:
            self.labyrinth_quantity += 1

            return "Игра окончена"

        lab.draw_labyrinth(matrix, (sx, sy), (fx, fy))

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
    
    def show_statictic(self):
        return f" Количество пройденных лабиринтов: {self.labyrinth_quantity}"