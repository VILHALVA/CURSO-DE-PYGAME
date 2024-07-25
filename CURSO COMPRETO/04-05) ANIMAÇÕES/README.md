# ANIMAÇÕES
Animações são uma parte essencial dos jogos e aplicativos gráficos, permitindo que objetos na tela se movam, mudem ou se transformem de maneiras visuais interessantes. Em Pygame, você pode criar animações de várias maneiras, desde a mudança de imagens (sprites) até a manipulação direta das propriedades dos objetos gráficos.

Aqui estão algumas abordagens comuns para criar animações em Pygame:

1. **Animação de Sprites (Imagens)**:
   - Utiliza uma série de imagens (frames) que representam diferentes etapas de uma animação.
   - Troca essas imagens em intervalos regulares para criar a ilusão de movimento.

2. **Animação de Propriedades**:
   - Altera propriedades como posição, tamanho, cor ou ângulo de um objeto ao longo do tempo para criar a animação.

## Exemplo de Animação de Sprites
Vamos criar um exemplo de animação onde um personagem (um sprite) se move para a direita e para a esquerda, alternando entre duas imagens (frames). Vamos supor que você tenha duas imagens de um personagem andando para a direita e para a esquerda.

1. **Preparar Imagens**:
   - Certifique-se de ter duas imagens para o sprite, por exemplo, `walk_right.png` e `walk_left.png`.

2. **Código de Animação de Sprites**:

```python
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Animação de Sprites')

# Configurações do jogo
FPS = 10
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)

# Carregar imagens
sprite_right = pygame.image.load('walk_right.png').convert_alpha()
sprite_left = pygame.image.load('walk_left.png').convert_alpha()
sprite_size = sprite_right.get_rect().size

# Configurações do sprite
sprite_x, sprite_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
sprite_speed = 5
direction = 'right'

# Lista de frames para animação
frames_right = [sprite_right]
frames_left = [sprite_left]

# Função principal do jogo
def main():
    global sprite_x, sprite_y, direction
    frame_index = 0
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
            sprite_x -= sprite_speed
        if keys[pygame.K_RIGHT]:
            direction = 'right'
            sprite_x += sprite_speed

        # Troca de frames para animação
        frame_index += 1
        if frame_index >= len(frames_right):
            frame_index = 0

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca

        # Desenha o sprite com base na direção
        if direction == 'right':
            screen.blit(frames_right[frame_index], (sprite_x, sprite_y))
        else:
            screen.blit(frames_left[frame_index], (sprite_x, sprite_y))

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
1. **Carregar Imagens**:
   - As imagens `walk_right.png` e `walk_left.png` são carregadas e armazenadas em variáveis.

2. **Listas de Frames**:
   - Criamos listas `frames_right` e `frames_left` que contêm os frames de animação para as direções direita e esquerda.

3. **Troca de Frames**:
   - No loop principal do jogo, alternamos entre os frames da animação com base na direção do movimento do jogador.

4. **Desenho na Tela**:
   - Dependendo da direção, desenhamos o sprite correspondente na tela.

## Exemplo de Animação de Propriedades
Vamos criar um exemplo de animação onde um quadrado muda sua posição e tamanho ao longo do tempo.

```python
import pygame
import sys
import math

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Animação de Propriedades')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurações do quadrado
square_size = 50
square_x = SCREEN_WIDTH // 2
square_y = SCREEN_HEIGHT // 2
max_size = 100
min_size = 50
size_change_speed = 0.05
angle = 0

# Função principal do jogo
def main():
    global square_size, square_x, square_y, angle
    running = True

    while running:
        # Gerenciamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualização da lógica do jogo
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
```

## Explicação do Código
1. **Animação de Tamanho**:
   - O tamanho do quadrado é ajustado usando uma função seno para criar um efeito de pulsação.

2. **Animação de Movimento**:
   - O quadrado se move em um caminho circular com base em um ângulo que é incrementado ao longo do tempo.

## Conclusão
Os exemplos acima mostram como criar animações em Pygame usando tanto sprites quanto propriedades. Você pode combinar essas técnicas para criar animações mais complexas e dinâmicas em seus projetos de jogos e gráficos. 