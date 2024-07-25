# DESENHANDO FIGURAS NA TELA
Desenhar figuras na tela é uma parte fundamental do desenvolvimento de jogos e gráficos com Pygame. Pygame oferece várias funções para desenhar formas geométricas, como linhas, retângulos, círculos e polígonos. Vou mostrar como você pode usar essas funções para desenhar diferentes figuras na tela e adicionar algumas interatividade básica.

## Funções para Desenhar Figuras em Pygame
Aqui estão algumas das funções principais para desenhar figuras:

1. **Retângulos**:
   - `pygame.draw.rect(surface, color, rect)`: Desenha um retângulo.

2. **Círculos**:
   - `pygame.draw.circle(surface, color, center, radius)`: Desenha um círculo.

3. **Linhas**:
   - `pygame.draw.line(surface, color, start_pos, end_pos, width)`: Desenha uma linha.

4. **Polígonos**:
   - `pygame.draw.polygon(surface, color, points)`: Desenha um polígono com a lista de pontos fornecida.

5. **Elipses**:
   - `pygame.draw.ellipse(surface, color, rect)`: Desenha uma elipse dentro do retângulo fornecido.

## Exemplo Prático
Vamos criar um exemplo de jogo onde diferentes figuras são desenhadas na tela e se movem com base na entrada do usuário.

```python
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Desenhando Figuras com Pygame')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configurações das figuras
player_size = 50
player_color = BLUE
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 5

circle_radius = 30
circle_color = RED
circle_x, circle_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4

# Função principal do jogo
def main():
    global player_x, player_y
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

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca

        # Desenha um retângulo
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
        
        # Desenha um círculo
        pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

        # Desenha uma linha
        pygame.draw.line(screen, BLACK, (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 5)

        # Desenha um polígono
        pygame.draw.polygon(screen, GREEN, [(100, 100), (150, 50), (200, 100), (150, 150)], 3)

        # Desenha uma elipse
        pygame.draw.ellipse(screen, BLACK, (300, 200, 100, 50))

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Executa a função principal do jogo
if __name__ == "__main__":
    main()
```

## Explicação do Código
1. **Configurações Iniciais**:
   - Inicializa o Pygame e configura a janela do jogo, as cores e as configurações das figuras.

2. **Movimentação do Jogador**:
   - O jogador é representado por um retângulo que pode ser movido com as teclas de seta.

3. **Desenho das Figuras**:
   - **Retângulo**: Desenhado usando `pygame.draw.rect()`.
   - **Círculo**: Desenhado usando `pygame.draw.circle()`.
   - **Linha**: Desenhada usando `pygame.draw.line()`.
   - **Polígono**: Desenhado usando `pygame.draw.polygon()`.
   - **Elipse**: Desenhada usando `pygame.draw.ellipse()`.

4. **Loop Principal do Jogo**:
   - Gerencia eventos, atualiza a lógica do jogo, desenha as figuras na tela e atualiza a tela com `pygame.display.flip()`.
   - Controla a taxa de quadros por segundo usando `clock.tick(FPS)`.

## Conclusão
Este exemplo demonstra como desenhar diferentes tipos de figuras na tela usando Pygame. Você pode usar essas funções para criar gráficos mais complexos e interativos em seus jogos e projetos. 