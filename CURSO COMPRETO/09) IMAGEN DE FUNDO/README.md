# IMAGEN DE FUNDO
Vamos analisar o código linha por linha de `./CODIGOS/CODIGO_1.py` para entender como ele funciona. Esse código usa a biblioteca Pygame para criar uma janela, carregar uma imagem de fundo e exibi-la continuamente até que o usuário feche a janela.

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
5. **`background = pygame.image.load("background.png").convert()`**: Carrega a imagem de fundo do arquivo "background.png" e converte o formato da imagem para otimizar a exibição. A função `pygame.image.load` carrega a imagem, e o método `.convert()` converte a imagem para o formato de pixels da tela, o que melhora o desempenho.

```python
while not done:
```
6. **`while not done:`**: Inicia um loop que continuará rodando enquanto `done` for `False`. Esse é o loop principal do jogo.

```python
    for event in pygame.event.get():
```
7. **`for event in pygame.event.get():`**: Inicia um loop que percorre todos os eventos que ocorreram desde a última chamada dessa função. A função `pygame.event.get()` retorna uma lista de eventos.

```python
        if event.type == pygame.QUIT:
            done = True
```
8. **`if event.type == pygame.QUIT:`**: Verifica se o evento capturado é do tipo `QUIT`, que é gerado quando o usuário tenta fechar a janela do jogo.
9. **`done = True`**: Se o evento `QUIT` for detectado, a variável `done` é definida como `True`, o que fará com que o loop principal termine na próxima iteração.

```python
    screen.blit(background, [0, 0])
```
10. **`screen.blit(background, [0, 0])`**: Desenha a imagem de fundo na tela na posição (0, 0). A função `blit` copia o conteúdo de uma superfície (neste caso, `background`) para outra superfície (neste caso, `screen`).

```python
    pygame.display.flip()
```
11. **`pygame.display.flip()`**: Atualiza a tela com tudo que foi desenhado desde a última chamada dessa função. Isso troca o buffer da tela e mostra a nova imagem.

```python
    clock.tick(60)
```
12. **`clock.tick(60)`**: Controla a taxa de atualização do jogo. Isso faz com que o loop principal espere o tempo necessário para manter uma taxa de 60 frames por segundo (FPS).

```python
pygame.quit()
```
13. **`pygame.quit()`**: Encerra o Pygame e fecha a janela do jogo. Isso deve ser chamado após o loop principal terminar para limpar corretamente os recursos do Pygame.

## Explicação Geral
- O código cria uma janela de jogo de 720x720 pixels.
- Carrega uma imagem de fundo e a exibe continuamente.
- O loop principal do jogo verifica eventos do usuário, especificamente se a janela foi fechada, e desenha a imagem de fundo na tela.
- A tela é atualizada 60 vezes por segundo, controlada pelo objeto `clock`.
- O loop termina quando o usuário fecha a janela, e então o Pygame é encerrado corretamente.