# MANUAL
## PASSO 1: INSTALAÇÃO DO PYTHON:
1. **Baixe o Python**:
   - Vá para o site oficial do Python: [python.org](https://www.python.org/).
   - Baixe a versão mais recente do Python 3 para o seu sistema operacional.

2. **Instale o Python**:
   - Siga as instruções do instalador.
   - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação para facilitar o uso do Python a partir do terminal ou prompt de comando.

## PASSO 2: INSTALAÇÃO DO PYGAME:
1. **Abra o Terminal ou Prompt de Comando**:
   - No Windows, você pode usar o "Prompt de Comando" ou "PowerShell".
   - No macOS e Linux, você pode usar o "Terminal".

2. **Instale o Pygame usando pip**:
   - Execute o seguinte comando para instalar o Pygame:
     ```bash
     pip install pygame
     ```

3. **Verifique a Instalação**:
   - Após a instalação, você pode verificar se o Pygame foi instalado corretamente executando:
     ```bash
     python -m pygame.examples.aliens
     ```
   - Isso deve abrir um pequeno jogo de exemplo. Se o jogo abrir, a instalação foi bem-sucedida.

## PASSO 3: CONFIGURAÇÃO DO AMBIENTE DE DESENVOLVIMENTO:
1. **Escolha um Editor de Texto ou IDE**:
   - Existem muitos editores de texto e IDEs disponíveis. Alguns dos mais populares são:
     - Visual Studio Code
     - PyCharm
     - Sublime Text
     - Atom

2. **Crie um Novo Projeto**:
   - Crie uma nova pasta em seu sistema para armazenar seu projeto.
   - Abra essa pasta no seu editor de texto ou IDE escolhido.

## PASSO 4: CRIAÇÃO DO PRIMEIRO PROJETO:
1. **Crie um Novo Arquivo Python**:
   - No seu editor de texto ou IDE, crie um novo arquivo chamado `main.py`.

2. **Adicione o Código Básico**:
   - Adicione o seguinte código ao `main.py` para criar uma janela básica com Pygame:
     ```python
     import pygame
     import sys

     # Inicializa o Pygame
     pygame.init()

     # Define as dimensões da janela
     screen = pygame.display.set_mode((640, 480))

     # Define o título da janela
     pygame.display.set_caption('Meu Primeiro Jogo com Pygame')

     # Define a cor de fundo (RGB)
     bg_color = (0, 0, 255)  # Azul

     # Loop principal do jogo
     while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
         
         # Preenche a tela com a cor de fundo
         screen.fill(bg_color)
         
         # Atualiza a tela
         pygame.display.flip()
     ```

3. **Execute o Projeto**:
   - No terminal ou prompt de comando, navegue até a pasta do seu projeto.
   - Execute o script `main.py`:
     ```bash
     python main.py
     ```
   - Isso abrirá uma janela azul com o título "Meu Primeiro Jogo com Pygame".

## PASSO 5: ADICIONAR UMA IMAGEM:
1. **Adicione uma Imagem ao Projeto**:
   - Salve uma imagem (por exemplo, `player.png`) na mesma pasta do seu `main.py`.

2. **Carregue e Exiba a Imagem**:
   - Atualize o `main.py` para carregar e desenhar a imagem na tela:
     ```python
     import pygame
     import sys

     # Inicializa o Pygame
     pygame.init()

     # Define as dimensões da janela
     screen = pygame.display.set_mode((640, 480))

     # Define o título da janela
     pygame.display.set_caption('Meu Primeiro Jogo com Pygame')

     # Define a cor de fundo (RGB)
     bg_color = (0, 0, 255)  # Azul

     # Carrega a imagem
     player_image = pygame.image.load('player.png')
     player_rect = player_image.get_rect()
     player_rect.topleft = (100, 100)

     # Loop principal do jogo
     while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
         
         # Preenche a tela com a cor de fundo
         screen.fill(bg_color)
         
         # Desenha a imagem na tela
         screen.blit(player_image, player_rect)
         
         # Atualiza a tela
         pygame.display.flip()
     ```

3. **Execute o Projeto Novamente**:
   - Execute novamente o script `main.py`:
     ```bash
     python main.py
     ```
   - Agora, a janela deve exibir a imagem `player.png` em uma posição específica.

## CONCLUSÃO:
Parabéns! Você instalou o Pygame, configurou seu ambiente de desenvolvimento e criou seu primeiro projeto básico com uma janela, cor de fundo e uma imagem. A partir daqui, você pode explorar mais funcionalidades do Pygame e desenvolver jogos mais complexos. 