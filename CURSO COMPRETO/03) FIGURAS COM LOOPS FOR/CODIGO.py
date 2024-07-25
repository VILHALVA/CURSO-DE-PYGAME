import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Colete os Círculos')

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
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 5

# Configurações dos itens
circle_radius = 20
circle_color = RED
items = []
item_spawn_time = 2000  # Tempo em milissegundos para spawnar um novo item
last_item_spawn_time = pygame.time.get_ticks()

# Pontuação
score = 0
font = pygame.font.SysFont(None, 36)

# Função para criar um novo item
def create_item():
    item_x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    item_y = random.randint(circle_radius, SCREEN_HEIGHT - circle_radius)
    items.append(pygame.Rect(item_x - circle_radius, item_y - circle_radius, circle_radius * 2, circle_radius * 2))

# Função para desenhar a pontuação na tela
def draw_score():
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

# Função principal do jogo
def main():
    global player_x, player_y, score, last_item_spawn_time
    running = True

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
        new_items = []
        for item in items:
            if player_rect.colliderect(item):
                score += 1
                player_speed += 0.1  # Aumenta a velocidade do jogador a cada ponto
            else:
                new_items.append(item)
        items = new_items

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca

        # Desenha o jogador
        pygame.draw.rect(screen, player_color, player_rect)

        # Desenha os itens
        for item in items:
            pygame.draw.circle(screen, circle_color, item.center, circle_radius)

        # Desenha uma grade de retângulos no fundo
        rect_width, rect_height = 60, 60
        spacing = 10
        for x in range(0, SCREEN_WIDTH, rect_width + spacing):
            for y in range(0, SCREEN_HEIGHT, rect_height + spacing):
                pygame.draw.rect(screen, BLACK, (x, y, rect_width, rect_height), 1)

        # Desenha a pontuação
        draw_score()

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Executa a função principal do jogo
if __name__ == "__main__":
    main()
