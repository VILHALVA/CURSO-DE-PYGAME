# DISPARANDO COM O MOUSE
O código de `./CODIGO/CODIGO.py` cria um jogo simples usando Pygame onde o jogador controla um personagem para disparar lasers e destruir meteoros que caem.

## Funcionamento do Código
1. **Importações e Definições**:
   ```python
   import pygame, random

   BLACK = (0, 0, 0)
   ```
   - Importa `pygame` e `random`.
   - Define a cor preta para o colorkey.

2. **Classe `Meteor`**:
   ```python
   class Meteor(pygame.sprite.Sprite):
       def __init__(self):
           super().__init__()
           self.image = pygame.image.load("meteor.png").convert()
           self.image.set_colorkey(BLACK)
           self.rect = self.image.get_rect()
   ```
   - Define a classe `Meteor`, que carrega a imagem do meteorito e define seu retângulo.

3. **Classe `Player`**:
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
           self.rect.y = 510
   ```
   - Define a classe `Player`, que carrega a imagem do jogador e atualiza a posição com base na posição do mouse. O jogador é fixado a uma altura y específica (`510`).

4. **Classe `Laser`**:
   ```python
   class Laser(pygame.sprite.Sprite):
       def __init__(self):
           super().__init__()
           self.image = pygame.image.load("laser.png").convert()
           self.rect = self.image.get_rect()

       def update(self):
           self.rect.y -= 4
   ```
   - Define a classe `Laser`, que carrega a imagem do laser e atualiza sua posição para cima.

5. **Configuração do Jogo**:
   ```python
   pygame.init()

   SCREEN_WIDTH = 900
   SCREEN_HEIGHT = 600
   screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
   clock = pygame.time.Clock()
   done = False
   score = 0

   meteor_list = pygame.sprite.Group()
   all_sprite_list = pygame.sprite.Group()
   laser_list = pygame.sprite.Group()

   for i in range(50):
       meteor = Meteor()
       meteor.rect.x = random.randrange(SCREEN_WIDTH - 20)
       meteor.rect.y = random.randrange(450) 

       meteor_list.add(meteor)
       all_sprite_list.add(meteor)

   player = Player()
   all_sprite_list.add(player)
   ```

   - Inicializa o Pygame e configura a tela.
   - Cria grupos de sprites para meteoros, lasers e todos os sprites.
   - Adiciona meteoros ao grupo de sprites e ao grupo de meteoros.
   - Adiciona o jogador ao grupo de sprites.

6. **Loop Principal do Jogo**:
   ```python
   while not done:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True

           if event.type == pygame.MOUSEBUTTONDOWN:
               laser = Laser()
               laser.rect.x = player.rect.x + 45
               laser.rect.y = player.rect.y - 20

               laser_list.add(laser)
               all_sprite_list.add(laser)

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

       screen.fill([255, 255, 255])
       all_sprite_list.draw(screen)
       pygame.display.flip()
       clock.tick(60)
   ```

   - **Eventos**: Verifica eventos, como clicar na tela para disparar lasers.
   - **Atualização**: Atualiza todos os sprites.
   - **Colisão**: Verifica se lasers colidem com meteoros e atualiza a pontuação. Remove lasers se eles saírem da tela.
   - **Desenho**: Preenche a tela de branco e desenha todos os sprites.
   - **FPS**: Mantém o jogo a 60 quadros por segundo.

