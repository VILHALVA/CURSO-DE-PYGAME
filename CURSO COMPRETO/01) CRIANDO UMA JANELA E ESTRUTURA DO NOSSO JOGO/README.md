# CRIANDO UMA JANELA E ESTRUTURA DO NOSSO JOGO
Vamos criar uma estrutura básica para um jogo com Pygame. Esta estrutura incluirá uma janela de jogo, um loop principal e o gerenciamento de eventos. Este é um bom ponto de partida para desenvolver qualquer jogo com Pygame.

## Passo 1: Estrutura Básica do Jogo
1. **Importações Necessárias**:
   - Vamos começar importando os módulos necessários.

2. **Inicialização do Pygame**:
   - Inicialize o Pygame e configure a janela do jogo.

3. **Loop Principal do Jogo**:
   - Crie um loop que continuará rodando até que o jogo seja fechado.
   - Dentro do loop, gerencie eventos, atualize o estado do jogo e desenhe na tela.

## Código Exemplo
```python
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Estrutura Básica do Jogo')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Função principal do jogo
def main():
    running = True

    while running:
        # Gerenciamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualização da lógica do jogo
        # Aqui você pode adicionar código para mover personagens, verificar colisões, etc.

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca
        # Aqui você pode adicionar código para desenhar sprites, textos, etc.

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
1. **Importações e Inicialização**:
   - `import pygame` e `import sys`: Importa os módulos Pygame e sys.
   - `pygame.init()`: Inicializa todos os módulos Pygame.

2. **Configuração da Janela**:
   - `SCREEN_WIDTH` e `SCREEN_HEIGHT`: Define a largura e altura da janela do jogo.
   - `screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))`: Cria a janela do jogo.
   - `pygame.display.set_caption('Estrutura Básica do Jogo')`: Define o título da janela.

3. **Configurações do Jogo**:
   - `FPS = 60`: Define a taxa de quadros por segundo.
   - `clock = pygame.time.Clock()`: Cria um objeto Clock para controlar a taxa de quadros.

4. **Loop Principal do Jogo**:
   - `while running:`: Loop principal que continuará rodando enquanto `running` for `True`.
   - `for event in pygame.event.get():`: Loop para gerenciar eventos, como fechar a janela.
   - `screen.fill(WHITE)`: Preenche a tela com a cor branca.
   - `pygame.display.flip()`: Atualiza a tela com tudo que foi desenhado.
   - `clock.tick(FPS)`: Controla a taxa de quadros para manter o jogo rodando a 60 FPS.

## Adicionando Funcionalidades
1. **Movimentação de Personagem**:
   - Adicione um personagem na tela e implemente a movimentação com as teclas de seta.

2. **Verificação de Colisões**:
   - Adicione objetos na tela e implemente a verificação de colisões entre o personagem e os objetos.

3. **Desenho de Sprites e Textos**:
   - Desenhe sprites (imagens) e textos na tela para criar um jogo mais complexo.

## Exemplo de Movimentação de Personagem
Vamos expandir o código para adicionar um personagem que pode se mover usando as teclas de seta.

```python
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Movimentação de Personagem')

# Configurações do jogo
FPS = 60
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações do personagem
player_size = 50
player_color = BLACK
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Função principal do jogo
def main():
    running = True

    while running:
        # Gerenciamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualização da lógica do jogo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Desenho na tela
        screen.fill(WHITE)  # Preenche a tela com a cor branca
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

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

## Explicação do Código Adicional
1. **Configurações do Personagem**:
   - `player_size`, `player_color`, `player_x`, `player_y`, `player_speed`: Configurações do personagem, incluindo tamanho, cor, posição inicial e velocidade de movimento.

2. **Movimentação do Personagem**:
   - `keys = pygame.key.get_pressed()`: Obtém o estado atual de todas as teclas do teclado.
   - `if keys[pygame.K_LEFT]:`: Move o personagem para a esquerda se a tecla de seta esquerda estiver pressionada.
   - `pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))`: Desenha o personagem como um retângulo na tela.

Este exemplo adiciona um personagem que pode se mover pela tela usando as teclas de seta. A partir daqui, você pode continuar expandindo seu jogo, adicionando mais funcionalidades, como colisões, inimigos, pontuação, e muito mais. 