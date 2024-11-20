#pip install pygame
import pygame
import random

# 초기화
pygame.init()

# 상수 정의
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

# 테트로미노 모양 정의
TETROMINOS = {
    'I': [[1, 1, 1, 1]],
    'L': [[1, 0, 0],
          [1, 1, 1]],
    'J': [[0, 0, 1],
          [1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'T': [[0, 1, 0],
          [1, 1, 1]]
}

COLORS = {
    'I': CYAN,
    'L': ORANGE,
    'J': BLUE,
    'O': YELLOW,
    'Z': RED,
    'S': GREEN,
    'T': PURPLE
}

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('테트리스')
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.create_piece()

    def create_piece(self):
        self.current_piece = random.choice(list(TETROMINOS.keys()))
        self.current_shape = TETROMINOS[self.current_piece]
        self.current_color = COLORS[self.current_piece]
        self.current_x = BOARD_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0

    def check_collision(self, x_offset=0, y_offset=0):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x + x_offset
                    new_y = self.current_y + y + y_offset
                    if (new_x < 0 or new_x >= BOARD_WIDTH or 
                        new_y >= BOARD_HEIGHT or 
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y][self.current_x + x] = self.current_color
        self.clear_lines()
        self.create_piece()
        if self.check_collision():
            self.reset_game()

    def clear_lines(self):
        lines_cleared = 0
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared * 100

    def rotate_piece(self):
        rotated = list(zip(*self.current_shape[::-1]))
        old_shape = self.current_shape
        self.current_shape = rotated
        if self.check_collision():
            self.current_shape = old_shape

    def draw(self):
        self.screen.fill(BLACK)
        
        # 보드에 있는 블록 그리기
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell,
                                   [x * BLOCK_SIZE, y * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 현재 조각 그리기
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.current_color,
                                   [(self.current_x + x) * BLOCK_SIZE,
                                    (self.current_y + y) * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 점수 표시
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    def run(self):
        fall_time = 0
        fall_speed = 1000  # 1초

        while True:
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            if fall_time >= fall_speed:
                self.current_y += 1
                if self.check_collision():
                    self.current_y -= 1
                    self.merge_piece()
                fall_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.check_collision(x_offset=-1):
                            self.current_x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if not self.check_collision(x_offset=1):
                            self.current_x += 1
                    elif event.key == pygame.K_DOWN:
                        if not self.check_collision(y_offset=1):
                            self.current_y += 1
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()

            self.draw()

if __name__ == '__main__':
    game = Tetris()
    game.run()