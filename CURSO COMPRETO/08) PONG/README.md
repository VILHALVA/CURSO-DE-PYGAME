# PONG
O código de `./CODIGO.py` é uma implementação básica de um jogo de Pong usando Pygame. Ele inclui dois jogadores que podem mover suas raquetes para cima e para baixo e uma bola que se move e rebate nas raquetes e nas bordas da tela.

## Inicialização
```python
import pygame
pygame.init()
```

- **`pygame`**: Biblioteca usada para criar jogos. O comando `pygame.init()` inicializa todos os módulos necessários do Pygame.

## Configurações e Cores
```python
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90
```

- **`black` e `white`**: Definem as cores usadas no jogo (preto e branco, respectivamente).
- **`screen_size`**: Define o tamanho da tela do jogo (800x600 pixels).
- **`player_width` e `player_height`**: Define as dimensões das raquetes dos jogadores.

## Configuração da Tela e Clock
```python
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
```

- **`screen`**: Cria uma janela de jogo com as dimensões especificadas.
- **`clock`**: Controla a taxa de atualização do jogo (neste caso, 60 quadros por segundo).

## Coordenadas e Velocidade dos Jogadores
```python
player1_x_coor = 50
player1_y_coor = screen_size[1] // 2 - player_height // 2
player1_y_speed = 0

player2_x_coor = screen_size[0] - player_width - 50
player2_y_coor = screen_size[1] // 2 - player_height // 2
player2_y_speed = 0
```

- **`player1_x_coor` e `player2_x_coor`**: Coordenadas X dos jogadores 1 e 2.
- **`player1_y_coor` e `player2_y_coor`**: Coordenadas Y centrais dos jogadores (ajustadas para centralizar verticalmente).
- **`player1_y_speed` e `player2_y_speed`**: Velocidades verticais dos jogadores (inicialmente 0).

## Coordenadas e Velocidade da Bola
```python
pelota_x = screen_size[0] // 2
pelota_y = screen_size[1] // 2
pelota_speed_x = 3
pelota_speed_y = 3
```

- **`pelota_x` e `pelota_y`**: Coordenadas iniciais da bola (centralizada na tela).
- **`pelota_speed_x` e `pelota_speed_y`**: Velocidades horizontais e verticais da bola.

## Pontuação
```python
score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 55)
```

- **`score1` e `score2`**: Pontuação dos jogadores 1 e 2.
- **`font`**: Fonte usada para desenhar o texto da pontuação.

## Função para Desenhar a Pontuação
```python
def draw_score():
    score_display = font.render(f"{score1} - {score2}", True, white)
    screen.blit(score_display, [screen_size[0] // 2 - score_display.get_width() // 2, 10])
```

- **`draw_score()`**: Função que desenha a pontuação na tela, centralizada no topo.

## Loop Principal do Jogo
```python
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # Jogador 1
            if event.key == pygame.K_w:
                player1_y_speed = -5
            if event.key == pygame.K_s:
                player1_y_speed = 5
            # Jogador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -5
            if event.key == pygame.K_DOWN:
                player2_y_speed = 5

        if event.type == pygame.KEYUP:
            # Jogador 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_y_speed = 0
            # Jogador 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_y_speed = 0

    # Atualiza posições dos jogadores
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    # Limita o movimento dos jogadores
    if player1_y_coor < 0:
        player1_y_coor = 0
    if player1_y_coor > screen_size[1] - player_height:
        player1_y_coor = screen_size[1] - player_height
    if player2_y_coor < 0:
        player2_y_coor = 0
    if player2_y_coor > screen_size[1] - player_height:
        player2_y_coor = screen_size[1] - player_height

    # Atualiza posição da bola
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    # Colisões com as bordas
    if pelota_y <= 0 or pelota_y >= screen_size[1]:
        pelota_speed_y *= -1

    # Colisões com as raquetes
    jugador1 = pygame.Rect(player1_x_coor, player1_y_coor, player_width, player_height)
    jugador2 = pygame.Rect(player2_x_coor, player2_y_coor, player_width, player_height)
    pelota = pygame.Rect(pelota_x, pelota_y, 10, 10)

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    # Pontuação
    if pelota_x < 0:
        score2 += 1
        pelota_x = screen_size[0] // 2
        pelota_y = screen_size[1] // 2
        pelota_speed_x *= -1
    if pelota_x > screen_size[0]:
        score1 += 1
        pelota_x = screen_size[0] // 2
        pelota_y = screen_size[1] // 2
        pelota_speed_x *= -1

    # Desenha tudo
    screen.fill(black)
    pygame.draw.rect(screen, white, jugador1)
    pygame.draw.rect(screen, white, jugador2)
    pygame.draw.ellipse(screen, white, pelota)
    draw_score()

    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
```

## Explicação Detalhada do Loop
1. **Eventos do Jogo**:
   - Captura eventos como o fechamento da janela (`QUIT`) e pressionamento/soltura de teclas para mover os jogadores.

2. **Atualização das Posições**:
   - Atualiza a posição vertical dos jogadores com base na velocidade.
   - Atualiza a posição da bola com base na velocidade.

3. **Limitação do Movimento dos Jogadores**:
   - Garante que os jogadores não saiam da tela.

4. **Colisões da Bola**:
   - A bola rebota nas bordas superior e inferior.
   - A bola rebota nas raquetes dos jogadores se colidir com elas.

5. **Pontuação**:
   - Adiciona um ponto ao jogador adversário se a bola sair pela lateral da tela e reinicializa a posição da bola.

6. **Desenho na Tela**:
   - Limpa a tela, desenha os jogadores, a bola e a pontuação atual.
   - Atualiza a tela com `pygame.display.flip()`.

7. **Controle de Taxa de Quadros**:
   - Limita a taxa de atualização do jogo para 60 quadros por segundo.
