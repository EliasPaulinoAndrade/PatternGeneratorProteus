# PatternGeneratorProteus
Nesse repositório estão alguns geradores de padrão para o proteus feitos na disciplina de MICROCONTROLADORES E MICROPROCESSADORES para automatizar tarefas com geradores de padrão. Os códigos de padrão gerados devem ser inseridos em geradores de padrão do proteus, exemplo: http://i.imgur.com/W5XudUw.png.

![](http://i.imgur.com/W5XudUw.png)

## Gerador de Padrão a partir de Imagem

### Pré-Requisitos:
* biblioteca PIL instalada( pip3 install pillow )

### Explicações:
O gerador irá percorrer a imagem chegando a cor de cada pixel, os pixels pretos significam leds da matrix ligados e os pixels branco são leds desligados. Serão necessários dois geradores de padrão para cada matrix 8x8 do proteus, um para ligar/desligar as linhas e outra para as colunas. O algoritmo gera um código que alterna as colunas acendendo os leds de cada linha correspondente, portanto o clock dos geradores de padrão devem ser setados de forma a dar continuidade a imagem.
Tenha certeza de que a imagem inserida tem no máximo 8 pixels de largura por 8 pixels de altura.

### Possibilidades:
É possível desenhar em mais de uma matrix8x8: dividindo uma imagem grande em blocos de 8x8 pixels, é possível desenhar imagens maiores.

## Gerador de Padrão a partir de Texto

### Explicações:
É bem mais simples que o outro, se trata apenas de uma leitura de texto e transformação em código do gerador de padrão do proteus, não foram colocadas proteções na quantidade de linhas para evitar overflow do gerador, portanto cheque se a palavra cabe no gerador antes de usar. É possível dividir uma palavra grande em vários geradores para desenhar um texto grande.
