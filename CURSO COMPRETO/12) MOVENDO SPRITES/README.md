# MOVENDO SPRITES
Vamos analisar o novo código de `./CODIGOS/CODIGO_2.py` linha por linha, com ênfase nas adições e mudanças, como a implementação do método `update` para o movimento dos meteoros e do jogador.

```python
import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
```
1. **`import pygame, random`**: Importa as bibliotecas Pygame e random.
2. **`WHITE = (255, 255, 255)`**: Define a cor branca como uma tupla RGB.
3. **`BLACK = (0, 0, 0)`**: Define a cor preta como uma tupla RGB.

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

        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)
```
4. **`class Meteor(pygame.sprite.Sprite):`**: Define a classe `Meteor` que herda da classe `Sprite` do Pygame.
5. **`def __init__(self):`**: Método inicializador da classe `Meteor`.
6. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
7. **`self.image = pygame.image.load("meteor.png").convert()`**: Carrega a imagem do meteoro e a converte para o formato de pixels da tela.
8. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente na imagem do meteoro.
9. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do meteoro.
10. **`def update(self):`**: Método que atualiza a posição do meteoro a cada frame.
11. **`self.rect.y += 1`**: Move o meteoro um pixel para baixo a cada frame.
12. **`if self.rect.y > 600:`**: Verifica se o meteoro saiu da tela pela parte inferior.
13. **`self.rect.y = -10`**: Reinicia a posição y do meteoro para aparecer novamente no topo da tela.
14. **`self.rect.x = random.randrange(900)`**: Define uma nova posição x aleatória para o meteoro.

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
15. **`class Player(pygame.sprite.Sprite):`**: Define a classe `Player` que herda da classe `Sprite` do Pygame.
16. **`def __init__(self):`**: Método inicializador da classe `Player`.
17. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
18. **`self.image = pygame.image.load("player.png").convert()`**: Carrega a imagem do jogador e a converte para o formato de pixels da tela.
19. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente na imagem do jogador.
20. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do jogador.
21. **`def update(self):`**: Método que atualiza a posição do jogador a cada frame.
22. **`mouse_pos = pygame.mouse.get_pos()`**: Obtém a posição atual do cursor do mouse na tela.
23. **`self.rect.x = mouse_pos[0]`**: Atualiza a posição x do jogador para seguir o cursor do mouse.
24. **`self.rect.y = mouse_pos[1]`**: Atualiza a posição y do jogador para seguir o cursor do mouse.

## Inicialização do Pygame e criação da janela
```python
pygame.init()

screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()
done = False
score = 0
```
25. **`pygame.init()`**: Inicializa todas as funções e módulos do Pygame.
26. **`screen = pygame.display.set_mode([900, 600])`**: Cria uma janela de 900x600 pixels.
27. **`clock = pygame.time.Clock()`**: Cria um objeto `Clock` para controlar a taxa de atualização (frames por segundo) do jogo.
28. **`done = False`**: Inicializa a variável `done` como `False`, usada para manter o loop do jogo rodando.
29. **`score = 0`**: Inicializa a variável `score` como 0, usada para rastrear a pontuação do jogador.

## Grupos de Sprites
```python
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
```
30. **`meteor_list = pygame.sprite.Group()`**: Cria um grupo de sprites para os meteoros.
31. **`all_sprite_list = pygame.sprite.Group()`**: Cria um grupo de sprites para todos os sprites (meteoros e jogador).

## Criação de Meteoros
```python
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)
```
32. **`for i in range(50):`**: Inicia um loop para criar 50 meteoros.
33. **`meteor = Meteor()`**: Cria uma instância da classe `Meteor`.
34. **`meteor.rect.x = random.randrange(900)`**: Define uma posição x aleatória para o meteoro dentro da largura da tela.
35. **`meteor.rect.y = random.randrange(600)`**: Define uma posição y aleatória para o meteoro dentro da altura da tela.
36. **`meteor_list.add(meteor)`**: Adiciona o meteoro ao grupo de meteoros.
37. **`all_sprite_list.add(meteor)`**: Adiciona o meteoro ao grupo de todos os sprites.

## Criação do Jogador
```python
player = Player()
all_sprite_list.add(player)
```
38. **`player = Player()`**: Cria uma instância da classe `Player`.
39. **`all_sprite_list.add(player)`**: Adiciona o jogador ao grupo de todos os sprites.

## Loop Principal do Jogo
```python
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
```
40. **`while not done:`**: Inicia um loop que continuará rodando enquanto `done` for `False`. Esse é o loop principal do jogo.
41. **`for event in pygame.event.get():`**: Inicia um loop que percorre todos os eventos que ocorreram desde a última chamada dessa função.
42. **`if event.type == pygame.QUIT:`**: Verifica se o evento capturado é do tipo `QUIT`, que é gerado quando o usuário tenta fechar a janela do jogo.
43. **`done = True`**: Se o evento `QUIT` for detectado, a variável `done` é definida como `True`, o que fará com que o loop principal termine na próxima iteração.

```python
    all_sprite_list.update()
```
44. **`all_sprite_list.update()`**: Chama o método `update` para todos os sprites no grupo `all_sprite_list`, atualizando suas posições.

```python
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
```
45. **`meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)`**: Verifica colisões entre o jogador e os meteoros. Se houver colisão, o meteoro é removido do grupo `meteor_list` (o parâmetro `True` indica que o sprite colidido deve ser removido).

```python
    for meteor in meteor_hit_list:
        score += 1
        print(score)
```
46. **`for meteor in meteor_hit_list:`**: Percorre todos os meteoros que colidiram com o jogador.
47. **`score += 1`**: Incrementa a pontuação em 1 para cada meteoro colidido.
48. **`print(score)`**: Imprime a pontuação atual no console.

```python
    screen.fill(WHITE)
```
49. **`screen.fill(WHITE)`**: Preenche a tela com a cor branca, apagando o conteúdo anterior.

```python
    all_sprite_list.draw(screen)
```
50. **`all_sprite_list.draw(screen)`**: Desenha todos os sprites no grupo `all_sprite_list` na tela.

```python
    pygame.display.flip()
```
51. **`pygame.display.flip()`**: Atualiza a tela com tudo que foi desenhado desde a última chamada dessa função. Isso troca o buffer da tela e mostra a nova imagem.

```python
    clock.tick(60)
```
52. **`clock.tick(60)`**: Controla a taxa de atualização do jogo, garantindo que ele rode a 60 frames por segundo (FPS).

```python
pygame.quit()
```
53. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo. Isso deve ser chamado após o loop principal terminar para limpar corretamente os recursos do Pygame.

## Resumo
Este código cria um jogo onde o jogador, controlado pelo mouse, deve evitar ou coletar meteoros que caem do topo da tela. Os meteoros reaparecem no topo após saírem da tela. A cada colisão entre o jogador e um meteoro, o meteoro é removido e a pontuação do jogador aumenta.