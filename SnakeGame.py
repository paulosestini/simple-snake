import random

class SnakeGame:
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.snake = [(random.randrange(0, self.cols), random.randrange(0, self.rows))]
        self.movements = {'U': (0, 1), 'D': (0, -1), 'L' : (-1, 0), 'R': (1, 0)}
        self.movement = None
        self.food = (random.randrange(0, self.cols), random.randrange(0, self.rows))
        self.score = 0

        # The food can't spawn on the same place as the snake
        while self.food == self.snake[0]:
            self.food = (random.randrange(0, self.cols), random.randrange(0, self.rows))

    def set_movement(self, move):
        if move in self.movements.keys():
            # Doesn't let the snake turn into itself
            if len(self.snake) > 1:
                head_x, head_y = self.snake[0]
                next_x, next_y = self.snake[1]
                if self.movements[move] == (next_x-head_x, next_y-head_y):
                    return
            self.movement = self.movements[move]

    def move(self):
        if not self.movement:
            return
        
        snake_copy = self.snake.copy()
        for i in range(1, len(self.snake)):
            self.snake[i] = snake_copy[i-1]
        x, y = self.snake[0]
        move_x, move_y = self.movement
        self.snake[0] = (x + move_x, y + move_y)

        if self.food == self.snake[0]:
            self.__add_segment()
            self.food = (random.randrange(0, self.cols), random.randrange(0, self.rows))
            self.score += 1
        
        # Food can't spawn on top of the snake
        while any([self.food == segment for segment in self.snake]):
            self.food = (random.randrange(0, self.cols), random.randrange(0, self.rows))

    def __add_segment(self):
        if len(self.snake) == 1:
            move_x, move_y = self.movement
            head_x, head_y = self.snake[0]
            self.snake.append((head_x - move_x, head_y - move_y))
        else:
            last_x, last_y = self.snake[len(self.snake)-1]
            before_x, before_y = self.snake[len(self.snake)-2]
            dir_x, dir_y = (last_x - before_x, last_y - before_y)
            self.snake.append((last_x + dir_x, last_y + dir_y))

    def game_ended(self):
        if any([count > 1 for count in [self.snake.count(x) for x in self.snake]]):
            return True
        x_s, y_s = zip(*self.snake)

        # Collision with the limits of the screen -- conditions
        c1 = any([x > self.cols for x in x_s])
        c2 = any([x < 0 for x in x_s])
        c3 = any([y > self.rows for y in y_s])
        c4 = any([y < 0 for y in y_s])
        return c1 or c2 or c3 or c4