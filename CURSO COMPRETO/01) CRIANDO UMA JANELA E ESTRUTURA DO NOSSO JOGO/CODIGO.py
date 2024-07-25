import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo de Coleta de Itens')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configurações do jogador
player_size = 50
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Configurações dos itens
item_size = 20
item_color = GREEN
item_spawn_time = 2000  # Tempo em milissegundos para spawnar um novo item

# Configurações da pontuação
score = 0
font = pygame.font.SysFont(None, 36)

# Lista para armazenar os itens
items = []

# Função para criar um novo item
def create_item():
    item_x = random.randint(0, SCREEN_WIDTH - item_size)
    item_y = random.randint(0, SCREEN_HEIGHT - item_size)
    items.append(pygame.Rect(item_x, item_y, item_size, item_size))

# Função para desenhar a pontuação na tela
def draw_score():
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

# Função principal do jogo
def main():
    global player_x, player_y, score
    running = True
    last_item_spawn_time = pygame.time.get_ticks()

    while running:
        # Gerenciamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualização da lógica do jogo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
            player_y += player_speed

        # Criação de novos itens
        current_time = pygame.time.get_ticks()
        if current_time - last_item_spawn_time > item_spawn_time:
            create_item()
            last_item_spawn_time = current_time

        # Verificação de colisões
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        items = [item for item in items if not player_rect.colliderect(item)]
        if len(items) < score:
            score += 1
            player_speed += 0.1  # Aumenta a velocidade do jogador a cada ponto

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca
        pygame.draw.rect(screen, player_color, player_rect)  # Desenha o jogador

        for item in items:
            pygame.draw.ellipse(screen, item_color, item)  # Desenha os itens

        draw_score()  # Desenha a pontuação

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Executa a função principal do jogo
if __name__ == "__main__":
    main()
