# SPRITES E CLASSES
Vamos analisar este código de `./CODIGOS/CODIGO_2.py` linha por linha. Este código usa a biblioteca Pygame para criar um jogo onde um jogador (controlado pelo mouse) deve evitar ou coletar meteoros que aparecem na tela.

```python
import pygame, random
```
1. **`import pygame, random`**: Importa as bibliotecas Pygame e random. Pygame é usada para criar o jogo, e random é usada para gerar posições aleatórias para os meteoros.

```python
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
```
2. **`WHITE = (255, 255, 255)`**: Define a cor branca como uma tupla RGB.
3. **`BLACK = (0, 0, 0)`**: Define a cor preta como uma tupla RGB.

```python
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
```
4. **`class Meteor(pygame.sprite.Sprite):`**: Define uma classe chamada `Meteor` que herda da classe `Sprite` do Pygame.
5. **`def __init__(self):`**: Método inicializador da classe `Meteor`.
6. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
7. **`self.image = pygame.image.load("meteor.png").convert()`**: Carrega a imagem do meteoro e a converte para o formato de pixels da tela para otimizar a exibição.
8. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente na imagem do meteoro.
9. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do meteoro.

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
```
10. **`class Player(pygame.sprite.Sprite):`**: Define uma classe chamada `Player` que herda da classe `Sprite` do Pygame.
11. **`def __init__(self):`**: Método inicializador da classe `Player`.
12. **`super().__init__()`**: Chama o inicializador da classe `Sprite`.
13. **`self.image = pygame.image.load("player.png").convert()`**: Carrega a imagem do jogador e a converte para o formato de pixels da tela para otimizar a exibição.
14. **`self.image.set_colorkey(BLACK)`**: Define a cor preta como transparente na imagem do jogador.
15. **`self.rect = self.image.get_rect()`**: Obtém o retângulo que circunscreve a imagem do jogador.

```python
pygame.init()
```
16. **`pygame.init()`**: Inicializa todas as funções e módulos do Pygame.

```python
screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()
done = False
score = 0
```
17. **`screen = pygame.display.set_mode([900, 600])`**: Cria uma janela de 900x600 pixels.
18. **`clock = pygame.time.Clock()`**: Cria um objeto `Clock` para controlar a taxa de atualização (frames por segundo) do jogo.
19. **`done = False`**: Inicializa a variável `done` como `False`, usada para manter o loop do jogo rodando.
20. **`score = 0`**: Inicializa a variável `score` como 0, usada para rastrear a pontuação do jogador.

```python
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
```
21. **`meteor_list = pygame.sprite.Group()`**: Cria um grupo de sprites para os meteoros.
22. **`all_sprite_list = pygame.sprite.Group()`**: Cria um grupo de sprites para todos os sprites (meteoros e jogador).

```python
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)
```
23. **`for i in range(50):`**: Inicia um loop para criar 50 meteoros.
24. **`meteor = Meteor()`**: Cria uma instância da classe `Meteor`.
25. **`meteor.rect.x = random.randrange(900)`**: Define uma posição x aleatória para o meteoro dentro da largura da tela.
26. **`meteor.rect.y = random.randrange(600)`**: Define uma posição y aleatória para o meteoro dentro da altura da tela.
27. **`meteor_list.add(meteor)`**: Adiciona o meteoro ao grupo de meteoros.
28. **`all_sprite_list.add(meteor)`**: Adiciona o meteoro ao grupo de todos os sprites.

```python
player = Player()
all_sprite_list.add(player)
```
29. **`player = Player()`**: Cria uma instância da classe `Player`.
30. **`all_sprite_list.add(player)`**: Adiciona o jogador ao grupo de todos os sprites.

```python
while not done:
```
31. **`while not done:`**: Inicia um loop que continuará rodando enquanto `done` for `False`. Esse é o loop principal do jogo.

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
```
32. **`for event in pygame.event.get():`**: Inicia um loop que percorre todos os eventos que ocorreram desde a última chamada dessa função.
33. **`if event.type == pygame.QUIT:`**: Verifica se o evento capturado é do tipo `QUIT`, que é gerado quando o usuário tenta fechar a janela do jogo.
34. **`done = True`**: Se o evento `QUIT` for detectado, a variável `done` é definida como `True`, o que fará com que o loop principal termine na próxima iteração.

```python
    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]
```
35. **`mouse_pos = pygame.mouse.get_pos()`**: Obtém a posição atual do cursor do mouse na tela.
36. **`player.rect.x = mouse_pos[0]`**: Atualiza a posição x do retângulo do jogador para a posição x do cursor do mouse.
37. **`player.rect.y = mouse_pos[1]`**: Atualiza a posição y do retângulo do jogador para a posição y do cursor do mouse.

```python
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
```
38. **`meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)`**: Verifica colisões entre o jogador e os meteoros. Se houver colisão, o meteoro é removido do grupo `meteor_list` (o parâmetro `True` indica que o sprite colidido deve ser removido).

```python
    for meteor in meteor_hit_list:
        score += 1
        print(score)
```
39. **`for meteor in meteor_hit_list:`**: Percorre todos os meteoros que colidiram com o jogador.
40. **`score += 1`**: Incrementa a pontuação em 1 para cada meteoro colidido.
41. **`print(score)`**: Imprime a pontuação atual no console.

```python
    screen.fill(WHITE)
```
42. **`screen.fill(WHITE)`**: Preenche a tela com a cor branca, apagando o conteúdo anterior.

```python
    all_sprite_list.draw(screen)
```
43. **`all_sprite_list.draw(screen)`**: Desenha todos os sprites no grupo `all_sprite_list` na tela.

```python
    pygame.display.flip()
```
44. **`pygame.display.flip()`**: Atualiza a tela com tudo que foi desenhado desde a última chamada dessa função. Isso troca o buffer da tela e mostra a nova imagem.

```python
    clock.tick(60)
```
45. **`clock.tick(60)`**: Controla a taxa de atualização do jogo, garantindo que ele rode a 60 frames por segundo (FPS).

```python
pygame.quit()
```
46. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo. Isso deve ser chamado após o loop principal terminar para limpar corretamente os recursos do Pygame.

## Resumo
Este código cria um jogo onde um jogador controlado pelo mouse deve evitar ou coletar meteoros que aparecem na tela. Os meteoros são gerados em posições aleatórias e, quando colidem com o jogador, são removidos e a pontuação é incrementada. A tela é atualizada continuamente até que o jogador feche a janela.