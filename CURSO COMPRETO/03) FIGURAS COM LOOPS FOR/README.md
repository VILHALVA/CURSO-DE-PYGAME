# FIGURAS COM LOOPS FOR
Utilizar loops `for` para desenhar figuras em Pygame é uma maneira eficiente de criar padrões repetitivos ou distribuir objetos de forma ordenada na tela. Vou mostrar alguns exemplos práticos de como você pode usar loops `for` para desenhar figuras.

## Exemplos de Figuras com Loops `for`
1. **Desenhando uma Grade de Retângulos**

   Vamos criar uma grade de retângulos preenchidos, que pode ser útil para criar um fundo ou um padrão.

   ```python
   import pygame
   import sys

   # Inicializa o Pygame
   pygame.init()

   # Configurações da janela
   SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   pygame.display.set_caption('Grade de Retângulos')

   # Configurações do jogo
   FPS = 60
   clock = pygame.time.Clock()

   # Cores
   WHITE = (255, 255, 255)
   BLUE = (0, 0, 255)

   # Tamanho dos retângulos e espaçamento
   rect_width, rect_height = 50, 50
   spacing = 10

   # Função principal do jogo
   def main():
       running = True

       while running:
           # Gerenciamento de eventos
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False

           # Desenho na tela
           screen.fill(WHITE)  # Preenche a tela com a cor branca

           # Desenha uma grade de retângulos
           for x in range(0, SCREEN_WIDTH, rect_width + spacing):
               for y in range(0, SCREEN_HEIGHT, rect_height + spacing):
                   pygame.draw.rect(screen, BLUE, (x, y, rect_width, rect_height))

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

   **Explicação**:
   - Usa dois loops `for` aninhados para criar uma grade de retângulos.
   - O primeiro loop itera sobre a largura da tela, e o segundo sobre a altura, desenhando um retângulo em cada posição.

2. **Desenhando um Padrão de Círculos**

   Vamos criar um padrão de círculos distribuídos em uma matriz.

   ```python
   import pygame
   import sys

   # Inicializa o Pygame
   pygame.init()

   # Configurações da janela
   SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   pygame.display.set_caption('Padrão de Círculos')

   # Configurações do jogo
   FPS = 60
   clock = pygame.time.Clock()

   # Cores
   WHITE = (255, 255, 255)
   RED = (255, 0, 0)

   # Tamanho dos círculos e espaçamento
   circle_radius = 20
   spacing = 60

   # Função principal do jogo
   def main():
       running = True

       while running:
           # Gerenciamento de eventos
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False

           # Desenho na tela
           screen.fill(WHITE)  # Preenche a tela com a cor branca

           # Desenha um padrão de círculos
           for x in range(circle_radius, SCREEN_WIDTH, spacing):
               for y in range(circle_radius, SCREEN_HEIGHT, spacing):
                   pygame.draw.circle(screen, RED, (x, y), circle_radius)

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

   **Explicação**:
   - Usa dois loops `for` aninhados para criar um padrão de círculos.
   - O primeiro loop itera sobre a largura da tela, e o segundo sobre a altura, desenhando um círculo em cada posição.

3. **Desenhando Polígonos em uma Matriz**

   Vamos desenhar uma matriz de triângulos.

   ```python
   import pygame
   import sys

   # Inicializa o Pygame
   pygame.init()

   # Configurações da janela
   SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   pygame.display.set_caption('Matriz de Triângulos')

   # Configurações do jogo
   FPS = 60
   clock = pygame.time.Clock()

   # Cores
   WHITE = (255, 255, 255)
   GREEN = (0, 255, 0)

   # Tamanho dos triângulos e espaçamento
   triangle_size = 50
   spacing = 70

   # Função para desenhar um triângulo
   def draw_triangle(surface, color, position, size):
       x, y = position
       pygame.draw.polygon(surface, color, [
           (x, y - size // 2),
           (x - size // 2, y + size // 2),
           (x + size // 2, y + size // 2)
       ])

   # Função principal do jogo
   def main():
       running = True

       while running:
           # Gerenciamento de eventos
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False

           # Desenho na tela
           screen.fill(WHITE)  # Preenche a tela com a cor branca

           # Desenha uma matriz de triângulos
           for x in range(triangle_size // 2, SCREEN_WIDTH, spacing):
               for y in range(triangle_size // 2, SCREEN_HEIGHT, spacing):
                   draw_triangle(screen, GREEN, (x, y), triangle_size)

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

   **Explicação**:
   - Usa dois loops `for` aninhados para desenhar triângulos em uma matriz.
   - A função `draw_triangle` desenha um triângulo em uma posição específica com base no tamanho fornecido.

## Conclusão
Estes exemplos demonstram como você pode usar loops `for` para criar padrões e distribuir figuras na tela. Isso é útil para criar backgrounds, padrões repetitivos ou para gerar múltiplos objetos de forma organizada em seus projetos com Pygame. Você pode ajustar os parâmetros e os padrões conforme necessário para atender às suas necessidades específicas. 