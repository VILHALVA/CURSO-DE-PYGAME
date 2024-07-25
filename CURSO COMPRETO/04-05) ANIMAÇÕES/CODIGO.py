import pygame
import sys
import math
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aventura do Personagem e Quadrado Pulsante')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Configurações do personagem
player_width, player_height = 50, 50
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 5
direction = 'right'

# Configurações do quadrado pulsante
square_size = 50
max_size = 100
min_size = 50
size_change_speed = 0.05
angle = 0
square_x = random.randint(0, SCREEN_WIDTH - max_size)
square_y = random.randint(0, SCREEN_HEIGHT - max_size)

# Função principal do jogo
def main():
    global player_x, player_y, direction, square_size, square_x, square_y, angle

    running = True

    while running:
        # Gerenciamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualização da lógica do jogo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = 'left'
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            direction = 'right'
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Animação do quadrado pulsante
        angle += size_change_speed
        if angle > 2 * math.pi:
            angle -= 2 * math.pi

        # Calcula o tamanho do quadrado com base em uma função seno
        square_size = min_size + (max_size - min_size) * (0.5 * (math.sin(angle) + 1))

        # Atualiza a posição do quadrado para se mover em um círculo
        square_x = SCREEN_WIDTH // 2 + 200 * math.cos(angle)
        square_y = SCREEN_HEIGHT // 2 + 200 * math.sin(angle)

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca

        # Desenha o personagem
        if direction == 'right':
            pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
        else:
            pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

        # Desenha o quadrado pulsante
        pygame.draw.rect(screen, RED, (square_x - square_size // 2, square_y - square_size // 2, square_size, square_size))

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Executa a função principal do jogo
if __name__ == "__main__":
    main()
