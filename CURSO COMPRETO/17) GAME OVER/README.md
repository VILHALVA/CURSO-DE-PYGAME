# GAME OVER
O código de `./CODIGO/CODIGO.py` cria um jogo simples em Pygame onde o jogador controla um personagem com o mouse para evitar meteoros que caem. Quando todos os meteoros são destruídos, o jogo termina e uma mensagem de "Game Over" é exibida. Vamos revisar cada parte do código e sua funcionalidade:

## Configurações e Importações
```python
import pygame, random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
```
1. **Importações**: Importa os módulos `pygame` e `random`.
2. **Constantes**: Define o tamanho da tela e as cores preta e branca.

## Classe `Meteor`
```python
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -10
            self.rect.x = random.randrange(SCREEN_WIDTH)
```
3. **`class Meteor(pygame.sprite.Sprite)`**: Define a classe `Meteor` que herda de `pygame.sprite.Sprite`.
4. **`def __init__(self):`**: Inicializa a imagem e o retângulo do meteoro.
5. **`def update(self):`**: Atualiza a posição do meteoro, movendo-o para baixo e reiniciando a posição quando ele sai da tela.

## Classe `Player`
```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]
```
6. **`class Player(pygame.sprite.Sprite)`**: Define a classe `Player` que herda de `pygame.sprite.Sprite`.
7. **`def __init__(self):`**: Inicializa a imagem e o retângulo do jogador.
8. **`def update(self):`**: Atualiza a posição do jogador para seguir a posição do mouse.

## Classe `Game`
```python
class Game(object):
    def __init__(self):
        self.game_over = False
        self.score = 0

        self.meteor_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(50):
            meteor = Meteor()
            meteor.rect.x = random.randrange(SCREEN_WIDTH)
            meteor.rect.y = random.randrange(SCREEN_HEIGHT)

            self.meteor_list.add(meteor)
            self.all_sprites_list.add(meteor)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()

            meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

            for meteor in meteor_hit_list:
                self.score += 1
                print(self.score)

            if len(self.meteor_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(WHITE)

        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, Click To Continue", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()
```
9. **`class Game(object)`**: Define a classe `Game` que controla a lógica do jogo.
10. **`def __init__(self):`**: Inicializa o jogo, criando meteoros e um jogador.
11. **`def process_events(self):`**: Processa eventos, reinicializa o jogo quando a tela é clicada após o fim do jogo.
12. **`def run_logic(self):`**: Atualiza a lógica do jogo, verifica colisões e define o fim do jogo se todos os meteoros forem destruídos.
13. **`def display_frame(self, screen):`**: Desenha o quadro atual na tela, exibindo a mensagem de "Game Over" se o jogo estiver terminado.

## Função Principal
```python
def main():
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
```
14. **`def main():`**: Função principal que inicializa o Pygame e executa o loop do jogo.
15. **`pygame.init()`**: Inicializa todos os módulos do Pygame.
16. **`screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])`**: Cria a tela do jogo.
17. **`done = False`**: Inicializa a variável `done` para controlar o loop principal.
18. **`clock = pygame.time.Clock()`**: Cria um objeto `Clock` para controlar a taxa de atualização (FPS).
19. **`game = Game()`**: Cria uma instância da classe `Game`.
20. **`while not done:`**: Loop principal do jogo que processa eventos, executa a lógica do jogo e exibe o quadro atual.
21. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo.

## Resumo
- O código define um jogo em que o jogador controla um personagem para evitar meteoros. Quando todos os meteoros são destruídos, o jogo exibe uma mensagem de "Game Over" e pode ser reiniciado ao clicar na tela.
- Utiliza a estrutura de classes para organizar o jogo: `Meteor` para os meteoros, `Player` para o jogador, e `Game` para a lógica do jogo.
- O loop principal (`main`) controla a execução do jogo, processando eventos, atualizando a lógica e desenhando a tela.