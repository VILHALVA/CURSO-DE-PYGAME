# KEYBOARD - TECLADO
## Estrutura do Projeto
1. **Configurações Iniciais**: Inicialização do Pygame e configuração da tela.
2. **Animação de Sprites**: O personagem se move e alterna entre imagens de caminhada.
3. **Animação de Propriedades**: Um quadrado que pulsa e se move ao redor da tela.
4. **Interatividade com o Mouse**: Mudança de direção do personagem e cor do quadrado ao clicar.
5. **Interatividade com o Teclado**: Movimento do personagem em todas as direções e efeito de salto.
6. **Gerenciamento de Eventos e Lógica do Jogo**: Controle do movimento do personagem, animação do quadrado e interatividade com o mouse e teclado.
7. **Desenho na Tela**: Atualização da tela com as animações e interatividade.

## Código Completo
```python
import pygame
import sys
import math
import random

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aventura do Personagem e Quadrado Pulsante com Interatividade do Mouse e Teclado')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Carregar imagens do personagem
sprite_right = pygame.image.load('walk_right.png').convert_alpha()
sprite_left = pygame.image.load('walk_left.png').convert_alpha()
sprite_size = sprite_right.get_rect().size

# Configurações do personagem
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 5
jump_speed = 15
gravity = 1
is_jumping = False
jump_velocity = 0
direction = 'right'
frames_right = [sprite_right]
frames_left = [sprite_left]

# Configurações do quadrado pulsante
square_size = 50
max_size = 100
min_size = 50
size_change_speed = 0.05
angle = 0
square_x = random.randint(0, SCREEN_WIDTH - max_size)
square_y = random.randint(0, SCREEN_HEIGHT - max_size)
square_color = RED

# Função para gerar uma cor aleatória
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Função principal do jogo
def main():
    global player_x, player_y, direction, square_size, square_x, square_y, angle, square_color, is_jumping, jump_velocity

    frame_index = 0
    running = True

    while running:
        # Gerenciamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if player_x <= mouse_x <= player_x + sprite_size[0] and player_y <= mouse_y <= player_y + sprite_size[1]:
                    # Muda a direção do personagem ao clicar nele
                    direction = 'left' if direction == 'right' else 'right'
                if square_x - square_size // 2 <= mouse_x <= square_x + square_size // 2 and square_y - square_size // 2 <= mouse_y <= square_y + square_size // 2:
                    # Muda a cor do quadrado ao clicar nele
                    square_color = random_color()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    jump_velocity = -jump_speed

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

        # Atualiza a animação dos frames do personagem
        frame_index += 1
        if frame_index >= len(frames_right):
            frame_index = 0

        # Lógica de salto
        if is_jumping:
            player_y += jump_velocity
            jump_velocity += gravity
            if player_y >= SCREEN_HEIGHT // 2:
                player_y = SCREEN_HEIGHT // 2
                is_jumping = False

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
            screen.blit(frames_right[frame_index], (player_x, player_y))
        else:
            screen.blit(frames_left[frame_index], (player_x, player_y))

        # Desenha o quadrado pulsante
        pygame.draw.rect(screen, square_color, (square_x - square_size // 2, square_y - square_size // 2, square_size, square_size))

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
   - Inicializa o Pygame e configura a tela do jogo.

2. **Animação de Sprites**:
   - O personagem usa imagens (`walk_right.png` e `walk_left.png`) para animar o movimento para a direita e para a esquerda. O sprite muda de imagem de acordo com a direção do movimento.

3. **Animação de Propriedades**:
   - Um quadrado pulsa (altera seu tamanho) com base em uma função seno.
   - O quadrado se move em um caminho circular ao redor da tela.

4. **Interatividade com o Mouse**:
   - Ao clicar no personagem, ele muda de direção.
   - Ao clicar no quadrado pulsante, ele muda de cor para uma cor aleatória.

5. **Interatividade com o Teclado**:
   - O personagem pode se mover para a esquerda, direita, cima e baixo usando as teclas do teclado.
   - Ao pressionar a tecla de espaço, o personagem realiza um salto. A lógica de salto é controlada por uma variável de velocidade e gravidade.

6. **Gerenciamento de Eventos e Lógica do Jogo**:
   - O personagem se move com base nas teclas pressionadas.
   - A animação do quadrado é atualizada a cada frame.
   - Eventos de clique do mouse e pressionamento de teclas são gerenciados para interatividade.

7. **Desenho na Tela**:
   - O fundo é preenchido com a cor branca.
   - O personagem e o quadrado pulsante são desenhados na tela.

## Recursos Necessários
- **Imagens do Sprite**: As imagens `walk_right.png` e `walk_left.png` devem estar no mesmo diretório que o script Python. Você pode usar qualquer imagem de um personagem caminhando para os exemplos.

## Conclusão
Este projeto mostra como implementar animações e interatividade com o mouse e teclado em Pygame, criando uma experiência de jogo mais rica e dinâmica. Você pode expandir este projeto adicionando mais elementos interativos, diferentes tipos de animações e aprimorando a lógica do jogo. 