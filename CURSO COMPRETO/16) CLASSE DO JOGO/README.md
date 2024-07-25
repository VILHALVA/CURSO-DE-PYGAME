# CLASSE DO JOGO
O código de `./CODIGO/CODIGO.py` organiza o jogo em uma estrutura mais modular, dividindo responsabilidades em classes e métodos. Vamos analisar as partes principais e como elas funcionam:

## Estrutura do Código
### Importações e Configurações Iniciais
```python
import pygame, random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
```
1. **`import pygame, random`**: Importa os módulos `pygame` e `random`.
2. **`SCREEN_WIDTH` e `SCREEN_HEIGHT`**: Define as dimensões da tela do jogo.
3. **`BLACK` e `WHITE`**: Define as cores preta e branca usando tuplas RGB.

### Classe `Meteor`
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
4. **`class Meteor(pygame.sprite.Sprite):`**: Define a classe `Meteor` que herda de `pygame.sprite.Sprite`.
5. **`def __init__(self):`**: Método inicializador da classe `Meteor`.
6. **`self.image = pygame.image.load("meteor.png").convert()`**: Carrega e converte a imagem do meteoro.
7. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente.
8. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do meteoro.
9. **`def update(self):`**: Atualiza a posição do meteoro a cada frame, movendo-o para baixo e reiniciando a posição quando sai da tela.

### Classe `Player`
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
10. **`class Player(pygame.sprite.Sprite):`**: Define a classe `Player` que herda de `pygame.sprite.Sprite`.
11. **`def __init__(self):`**: Método inicializador da classe `Player`.
12. **`self.image = pygame.image.load("player.png").convert()`**: Carrega e converte a imagem do jogador.
13. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente.
14. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do jogador.
15. **`def update(self):`**: Atualiza a posição do jogador para seguir a posição do mouse.

### Classe `Game`
```python
class Game(object):
    def __init__(self):
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

        return False

    def run_logic(self):
        self.all_sprites_list.update()

        meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

        for meteor in meteor_hit_list:
            self.score += 1
            print(self.score)

    def display_frame(self, screen):
        screen.fill(WHITE)
        self.all_sprites_list.draw(screen)
        pygame.display.flip()
```
16. **`class Game(object):`**: Define a classe `Game` que controla a lógica do jogo.
17. **`def __init__(self):`**: Método inicializador da classe `Game`.
18. **`self.score = 0`**: Inicializa a pontuação como 0.
19. **`self.meteor_list = pygame.sprite.Group()`**: Cria um grupo para os meteoros.
20. **`self.all_sprites_list = pygame.sprite.Group()`**: Cria um grupo para todos os sprites.
21. **`for i in range(50):`**: Cria 50 meteoros e os adiciona aos grupos de sprites.
22. **`self.player = Player()`**: Cria uma instância de `Player` e a adiciona ao grupo de todos os sprites.
23. **`def process_events(self):`**: Processa eventos, retornando `True` se o evento for `QUIT`.
24. **`def run_logic(self):`**: Atualiza todos os sprites e verifica colisões entre o jogador e os meteoros. Aumenta a pontuação e imprime no console quando um meteoro é atingido.
25. **`def display_frame(self, screen):`**: Preenche a tela com a cor branca, desenha todos os sprites e atualiza a tela.

### Função Principal
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
26. **`def main():`**: Função principal que inicializa o Pygame e configura o loop do jogo.
27. **`pygame.init()`**: Inicializa todos os módulos do Pygame.
28. **`screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])`**: Cria a janela do jogo.
29. **`done = False`**: Inicializa a variável `done` como `False` para controlar o loop principal.
30. **`clock = pygame.time.Clock()`**: Cria um objeto `Clock` para controlar a taxa de atualização (FPS).
31. **`game = Game()`**: Cria uma instância da classe `Game`.
32. **`while not done:`**: Loop principal do jogo.
33. **`done = game.process_events()`**: Processa eventos e define `done` como `True` se o evento for `QUIT`.
34. **`game.run_logic()`**: Atualiza a lógica do jogo.
35. **`game.display_frame(screen)`**: Desenha o frame atual na tela.
36. **`clock.tick(60)`**: Controla a taxa de atualização do jogo a 60 FPS.
37. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo.

## Resumo
Este código cria um jogo simples onde meteoros caem da parte superior da tela e o jogador controla um personagem que se move com o mouse. O objetivo é destruir meteoros (por meio de colisões) e aumentar a pontuação. A estrutura modular em classes (`Meteor`, `Player`, e `Game`) torna o código mais organizado e facilita a manutenção e expansão do jogo.