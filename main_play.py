import pygame
import random
import math

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Беги от мини-Годзил!")

# Цвета
WHITE = (255, 255, 255)
PLAYER_COLOR = (10, 190, 255)
MONSTER_COLOR = (0, 10, 30)
MONSTER_GREEN = (0, 10, 0)
BACKGROUND_COLOR = (100, 100, 190)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки игрока
PLAYER_SIZE = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * PLAYER_SIZE]
player_speed = 5

# Настройки монстров
MONSTER_SIZE = 50
monster_speed = 2
monsters = []

# Спавн монстров
def spawn_monster():
    x_pos = random.randint(0, WIDTH - MONSTER_SIZE)
    y_pos = -MONSTER_SIZE
    monsters.append([x_pos, y_pos])

# Функция для рисования игрока (простой человечек)
def draw_player(position):
    x, y = position
    # Тело
    pygame.draw.rect(WIN, PLAYER_COLOR, (x + 10, y + 20, 30, 30))
    # Голова
    pygame.draw.circle(WIN, PLAYER_COLOR, (x + 25, y + 10), 15)
    # Руки
    pygame.draw.line(WIN, PLAYER_COLOR, (x + 10, y + 25), (x, y + 25), 3)
    pygame.draw.line(WIN, PLAYER_COLOR, (x + 40, y + 25), (x + 50, y + 25), 3)
    # Ноги
    pygame.draw.line(WIN, PLAYER_COLOR, (x + 20, y + 50), (x + 20, y + 60), 3)
    pygame.draw.line(WIN, PLAYER_COLOR, (x + 30, y + 50), (x + 30, y + 60), 3)

# Функция для рисования монстра (мини-Годзилла)
def draw_monster(position):
    x, y = position
    # Туловище
    pygame.draw.rect(WIN, MONSTER_GREEN, (x, y + 20, MONSTER_SIZE, 30))
    # Голова
    pygame.draw.circle(WIN, MONSTER_GREEN, (x + MONSTER_SIZE // 2, y + 10), 15)
    # Глаза
    pygame.draw.circle(WIN, WHITE, (x + MONSTER_SIZE // 2 - 5, y + 10 - 5), 5)
    pygame.draw.circle(WIN, WHITE, (x + MONSTER_SIZE // 2 + 5, y + 10 - 5), 5)
    # Рога
    pygame.draw.polygon(WIN, RED, [(x + 15, y + 5), (x + 10, y), (x + 20, y + 5)])
    pygame.draw.polygon(WIN, RED, [(x + MONSTER_SIZE - 15, y + 5), (x + MONSTER_SIZE - 10, y), (x + MONSTER_SIZE - 20, y + 5)])
    # Руки
    pygame.draw.line(WIN, MONSTER_GREEN, (x + 0, y + 25), (x - 10, y + 35), 3)
    pygame.draw.line(WIN, MONSTER_GREEN, (x + MONSTER_SIZE, y + 25), (x + MONSTER_SIZE + 10, y + 35), 3)
    # Ноги
    pygame.draw.line(WIN, MONSTER_GREEN, (x + 15, y + 50), (x + 15, y + 60), 3)
    pygame.draw.line(WIN, MONSTER_GREEN, (x + MONSTER_SIZE - 15, y + 50), (x + MONSTER_SIZE - 15, y + 60), 3)

# Функция для проверки столкновений
def is_collision(player_pos, monster_pos):
    p_x, p_y = player_pos
    m_x, m_y = monster_pos

    # Простая проверка пересечения прямоугольников
    if (p_x < m_x + MONSTER_SIZE and p_x + PLAYER_SIZE > m_x and
        p_y < m_y + MONSTER_SIZE and p_y + PLAYER_SIZE > m_y):
        return True
    return False

# Основной цикл игры
def game_loop():
    clock = pygame.time.Clock()
    run = True
    spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_event, 2000)  # Спавнить монстра каждые 2 секунды

    while run:
        clock.tick(60)  # Ограничение до 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == spawn_event:
                spawn_monster()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] - player_speed > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] + player_speed < WIDTH - PLAYER_SIZE:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] - player_speed > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] + player_speed < HEIGHT - PLAYER_SIZE:
            player_pos[1] += player_speed

        # Обновление позиций монстров
        for monster in monsters:
            monster[1] += monster_speed
            # Простая логика движения монстров к игроку
            if monster[0] < player_pos[0]:
                monster[0] += 1
            elif monster[0] > player_pos[0]:
                monster[0] -= 1

        # Проверка столкновений
        for monster in monsters:
            if is_collision(player_pos, monster):
                print("Игра окончена!")
                run = False

        # Удаление монстров, вышедших за экран
        monsters[:] = [m for m in monsters if m[1] < HEIGHT]

        # Рендеринг
        WIN.fill(BACKGROUND_COLOR)
        draw_player(player_pos)
        for monster in monsters:
            draw_monster(monster)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game_loop()