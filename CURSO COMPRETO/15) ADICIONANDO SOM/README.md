# ADICIONANDO SOM
Este código de `./CODIGO/CODIGO.py` é uma versão aprimorada do jogo de tiro, que agora inclui um efeito sonoro quando o jogador dispara um laser. Vamos detalhar o código e as alterações feitas para incluir o som.

## Importações e Configurações Iniciais
```python
import pygame, random

BLACK = (0, 0, 0)
```
1. **`import pygame, random`**: Importa os módulos `pygame` e `random`.
2. **`BLACK = (0, 0, 0)`**: Define a cor preta usando uma tupla RGB.

## Definição das Classes dos Sprites
### Classe `Meteor`
```python
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
```
3. **`class Meteor(pygame.sprite.Sprite):`**: Define a classe `Meteor` que herda de `pygame.sprite.Sprite`.
4. **`def __init__(self):`**: Método inicializador da classe `Meteor`.
5. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
6. **`self.image = pygame.image.load("meteor.png").convert()`**: Carrega e converte a imagem do meteoro.
7. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente.
8. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do meteoro.

### Classe `Player`
```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    def changespeed(self, x):
        self.speed_x += x

    def update(self):
        self.rect.x += self.speed_x
        player.rect.y = 510
```
9. **`class Player(pygame.sprite.Sprite):`**: Define a classe `Player` que herda de `pygame.sprite.Sprite`.
10. **`def __init__(self):`**: Método inicializador da classe `Player`.
11. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
12. **`self.image = pygame.image.load("player.png").convert()`**: Carrega e converte a imagem do jogador.
13. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente.
14. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do jogador.
15. **`self.speed_x = 0`**: Inicializa a velocidade horizontal do jogador como 0.
16. **`self.speed_y = 0`**: Inicializa a velocidade vertical do jogador como 0.
17. **`def changespeed(self, x):`**: Método que altera a velocidade horizontal do jogador.
18. **`self.speed_x += x`**: Adiciona `x` à velocidade horizontal.
19. **`def update(self):`**: Atualiza a posição do jogador a cada frame.
20. **`self.rect.x += self.speed_x`**: Atualiza a posição x do jogador com base na velocidade horizontal.
21. **`self.rect.y = 510`**: Define a posição y do jogador fixamente em 510.

### Classe `Laser`
```python
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 4
```
22. **`class Laser(pygame.sprite.Sprite):`**: Define a classe `Laser` que herda de `pygame.sprite.Sprite`.
23. **`def __init__(self):`**: Método inicializador da classe `Laser`.
24. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
25. **`self.image = pygame.image.load("laser.png").convert()`**: Carrega e converte a imagem do laser.
26. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do laser.
27. **`def update(self):`**: Atualiza a posição do laser a cada frame.
28. **`self.rect.y -= 4`**: Move o laser para cima a uma taxa de 4 pixels por frame.

## Inicialização do Pygame e Criação da Janela
```python
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
done = False
score = 0
```
29. **`pygame.init()`**: Inicializa todos os módulos do Pygame.
30. **`SCREEN_WIDTH = 900`**: Define a largura da tela.
31. **`SCREEN_HEIGHT = 600`**: Define a altura da tela.
32. **`screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])`**: Cria a janela do jogo com as dimensões especificadas.
33. **`clock = pygame.time.Clock()`**: Cria um objeto `Clock` para controlar a taxa de atualização (FPS) do jogo.
34. **`done = False`**: Inicializa a variável `done` como `False` para controlar o loop principal do jogo.
35. **`score = 0`**: Inicializa a pontuação como 0.

## Grupos de Sprites
```python
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
```
36. **`meteor_list = pygame.sprite.Group()`**: Cria um grupo de sprites para os meteoros.
37. **`all_sprite_list = pygame.sprite.Group()`**: Cria um grupo de sprites para todos os sprites (meteoros, jogador e lasers).
38. **`laser_list = pygame.sprite.Group()`**: Cria um grupo de sprites para os lasers.

## Criação de Meteoros
```python
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(SCREEN_WIDTH - 20)
    meteor.rect.y = random.randrange(450) 

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)
```
39. **`for i in range(50):`**: Inicia um loop para criar 50 meteoros.
40. **`meteor = Meteor()`**: Cria uma instância de `Meteor`.
41. **`meteor.rect.x = random.randrange(SCREEN_WIDTH - 20)`**: Define a posição x aleatória para o meteoro, evitando que saia da tela.
42. **`meteor.rect.y = random.randrange(450)`**: Define a posição y aleatória para o meteoro.
43. **`meteor_list.add(meteor)`**: Adiciona o meteoro ao grupo de meteoros.
44. **`all_sprite_list.add(meteor)`**: Adiciona o meteoro ao grupo de todos os sprites.

## Criação do Jogador
```python
player = Player()
all_sprite_list.add(player)
```
45. **`player = Player()`**: Cria uma instância de `Player`.
46. **`all_sprite_list.add(player)`**: Adiciona o jogador ao grupo de todos os sprites.

## Configuração do Som
```python
sound = pygame.mixer.Sound("laser5.ogg")
```
47. **`sound = pygame.mixer.Sound("laser5.ogg")`**: Carrega o efeito sonoro do laser.

## Loop Principal do Jogo
```python
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 20

                laser_list.add(laser)
                all_sprite_list.add(laser)
                sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3)
```
48. **`while not done:`**: Inicia o loop principal do jogo que continua enquanto `done` for `False`.
49. **`for event in pygame.event.get():`**: Itera sobre todos os eventos que ocorreram desde a última chamada dessa função.
50. **`if event.type == pygame.QUIT:`**: Verifica se o evento é do tipo `QUIT` (o usuário tentou fechar a janela).
51. **`done = True`**: Se o evento for `QUIT`, define `done` como `True` para sair do loop principal.

52. **`if event.type == pygame.KEYDOWN:`**: Verifica se uma tecla foi pressionada.
53. **`if event.key == pygame.K_LEFT:`**: Se tecla pressionada for a seta para a esquerda, chama `player.changespeed(-3)` para mover o jogador para a esquerda.
54. **`if event.key == pygame.K_RIGHT:`**: Se a tecla pressionada for a seta para a direita, chama `player.changespeed(3)` para mover o jogador para a direita.
55. **`if event.key == pygame.K_SPACE:`**: Se a tecla pressionada for a barra de espaço, cria um novo laser e define sua posição inicial em relação ao jogador. Adiciona o laser aos grupos de sprites e toca o efeito sonoro.

56. **`if event.type == pygame.KEYUP:`**: Verifica se uma tecla foi solta.
57. **`if event.key == pygame.K_LEFT:`**: Se a tecla solta for a seta para a esquerda, chama `player.changespeed(3)` para parar o movimento para a esquerda.
58. **`if event.key == pygame.K_RIGHT:`**: Se a tecla solta for a seta para a direita, chama `player.changespeed(-3)` para parar o movimento para a direita.

## Atualização dos Sprites e Verificação de Colisões
```python
all_sprite_list.update() 

for laser in laser_list:
    meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)    
    for meteor in meteor_hit_list:
        all_sprite_list.remove(laser)
        laser_list.remove(laser)
        score += 1
        print(score)
    if laser.rect.y < -10:
        all_sprite_list.remove(laser)
        laser_list.remove(laser)
```
59. **`all_sprite_list.update()`**: Atualiza todos os sprites, chamando o método `update` de cada um deles.
60. **`for laser in laser_list:`**: Itera sobre cada laser no grupo de lasers.
61. **`meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)`**: Verifica colisões entre o laser e os meteoros. O parâmetro `True` remove os meteoros que colidirem com o laser.
62. **`for meteor in meteor_hit_list:`**: Itera sobre os meteoros que colidiram com o laser.
63. **`all_sprite_list.remove(laser)`**: Remove o laser do grupo de todos os sprites.
64. **`laser_list.remove(laser)`**: Remove o laser do grupo de lasers.
65. **`score += 1`**: Incrementa a pontuação em 1.
66. **`print(score)`**: Imprime a pontuação atual no console.
67. **`if laser.rect.y < -10:`**: Verifica se o laser saiu da tela pela parte superior (posicionamento y menor que -10).
68. **`all_sprite_list.remove(laser)`**: Remove o laser do grupo de todos os sprites.
69. **`laser_list.remove(laser)`**: Remove o laser do grupo de lasers.

## Desenho na Tela e Atualização
```python
screen.fill([255, 255, 255])

all_sprite_list.draw(screen)

pygame.display.flip()
clock.tick(60)
```
70. **`screen.fill([255, 255, 255])`**: Preenche a tela com a cor branca antes de desenhar os sprites.
71. **`all_sprite_list.draw(screen)`**: Desenha todos os sprites na tela.
72. **`pygame.display.flip()`**: Atualiza a tela com o conteúdo desenhado.
73. **`clock.tick(60)`**: Controla a taxa de atualização do jogo, garantindo que ele rode a 60 frames por segundo (FPS).

## Encerramento do Pygame
```python
pygame.quit()
```
74. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo. Deve ser chamado após o loop principal terminar para liberar recursos do Pygame.

## Resumo
Este código define um jogo em que o jogador controla um personagem que se move horizontalmente usando as teclas de seta e atira lasers com a barra de espaço. Meteoros caem do topo da tela, e o objetivo é destruir esses meteoros com os lasers. O código agora inclui um efeito sonoro que toca sempre que um laser é disparado. A cada colisão entre um laser e um meteoro, a pontuação aumenta e o meteoro é removido da tela. O jogo continua até que o usuário feche a janela.