# MOVENDO IMAGENS
Vamos explicar este código linha por linha de `./CODIGOS/CODIGO_2.py`, com as modificações que incluem a adição de um sprite do jogador que segue o cursor do mouse.

```python
import pygame
```
1. **`import pygame`**: Importa a biblioteca Pygame, que é usada para criar jogos e outras aplicações multimídia em Python.

```python
screen = pygame.display.set_mode([720, 720])
```
2. **`screen = pygame.display.set_mode([720, 720])`**: Cria uma janela de 720x720 pixels e atribui à variável `screen`. A função `pygame.display.set_mode` define o tamanho da janela onde o jogo será exibido.

```python
clock = pygame.time.Clock()
```
3. **`clock = pygame.time.Clock()`**: Cria um objeto `Clock` para controlar a taxa de atualização (frames por segundo) do jogo. Isso é útil para garantir que o jogo rode de forma consistente em diferentes computadores.

```python
done = False
```
4. **`done = False`**: Inicializa a variável `done` como `False`. Essa variável é usada como condição para manter o loop do jogo rodando. Quando `done` se torna `True`, o loop é encerrado.

```python
background = pygame.image.load("background.png").convert()
```
5. **`background = pygame.image.load("background.png").convert()`**: Carrega a imagem de fundo do arquivo "background.png" e a converte para o formato de pixels da tela para otimizar a exibição.

```python
player = pygame.image.load("player.png").convert()
player.set_colorkey([0, 0, 0])
```
6. **`player = pygame.image.load("player.png").convert()`**: Carrega a imagem do jogador do arquivo "player.png" e a converte para o formato de pixels da tela para otimizar a exibição.
7. **`player.set_colorkey([0, 0, 0])`**: Define a cor de transparência para a imagem do jogador. Pixels com a cor `[0, 0, 0]` (preto) serão transparentes quando a imagem for desenhada na tela.

```python
while not done:
```
8. **`while not done:`**: Inicia um loop que continuará rodando enquanto `done` for `False`. Esse é o loop principal do jogo.

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
```
9. **`for event in pygame.event.get():`**: Inicia um loop que percorre todos os eventos que ocorreram desde a última chamada dessa função. A função `pygame.event.get()` retorna uma lista de eventos.
10. **`if event.type == pygame.QUIT:`**: Verifica se o evento capturado é do tipo `QUIT`, que é gerado quando o usuário tenta fechar a janela do jogo.
11. **`done = True`**: Se o evento `QUIT` for detectado, a variável `done` é definida como `True`, o que fará com que o loop principal termine na próxima iteração.

```python
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
```
12. **`mouse_pos = pygame.mouse.get_pos()`**: Obtém a posição atual do cursor do mouse na tela. Retorna uma tupla com as coordenadas (x, y).
13. **`x = mouse_pos[0]`**: Armazena a coordenada x do cursor do mouse na variável `x`.
14. **`y = mouse_pos[1]`**: Armazena a coordenada y do cursor do mouse na variável `y`.

```python
    screen.blit(background, [0, 0])
```
15. **`screen.blit(background, [0, 0])`**: Desenha a imagem de fundo na tela na posição (0, 0). A função `blit` copia o conteúdo de uma superfície (neste caso, `background`) para outra superfície (neste caso, `screen`).

```python
    screen.blit(player, [x, y])
```
16. **`screen.blit(player, [x, y])`**: Desenha a imagem do jogador na tela na posição definida pelo cursor do mouse. A função `blit` copia o conteúdo de uma superfície (neste caso, `player`) para outra superfície (neste caso, `screen`).

```python
    pygame.display.flip()
```
17. **`pygame.display.flip()`**: Atualiza a tela com tudo que foi desenhado desde a última chamada dessa função. Isso troca o buffer da tela e mostra a nova imagem.

```python
    clock.tick(60)
```
18. **`clock.tick(60)`**: Controla a taxa de atualização do jogo. Isso faz com que o loop principal espere o tempo necessário para manter uma taxa de 60 frames por segundo (FPS).

```python
pygame.quit()
```
19. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo. Isso deve ser chamado após o loop principal terminar para limpar corretamente os recursos do Pygame.

## Resumo
Esse código cria uma janela de 720x720 pixels, carrega uma imagem de fundo e uma imagem do jogador, e desenha ambas na tela. A posição da imagem do jogador segue a posição do cursor do mouse. O jogo continua rodando até que o usuário feche a janela. A taxa de atualização é mantida em 60 frames por segundo.