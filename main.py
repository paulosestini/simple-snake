import SnakeGame
import pygame

pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
commands = {pygame.K_UP: 'D', pygame.K_DOWN: 'U', pygame.K_LEFT: 'L', pygame.K_RIGHT: 'R'}
game = SnakeGame.SnakeGame()
rect_w, rect_h = width/game.cols, height/game.rows
snake_color = (255, 255, 255)
food_color = (255, 0, 0)

clock = pygame.time.Clock()


font = pygame.font.SysFont('dejavusans', 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in commands.keys():
                game.set_movement(commands[event.key])

    screen.fill((0, 0, 0))

    game.move()
    for segment in game.snake:
        x, y = segment
        rectangle_info = (x*rect_w, y*rect_h, rect_w, rect_h)
        pygame.draw.rect(screen, snake_color, rectangle_info)

    food_x, food_y = game.food
    pygame.draw.rect(screen, food_color, (food_x*rect_w, food_y*rect_h, rect_w, rect_h))

    # Score
    text = font.render('Score: ' + str(game.score), True, (255, 255, 255))
    screen.blit(text,
        (width - 1.2*text.get_width(), 0.5*text.get_height()))

    pygame.display.flip()

    if game.game_ended(): 
        running = False

    clock.tick(10)