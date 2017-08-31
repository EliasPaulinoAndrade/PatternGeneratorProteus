import os, sys
from PIL import Image

class RepresentacaoFrame:
       def __init__(self, bits):
              self.bits = bits
class GeradorDePadrao:
       def __init__(self, painelDePixels, cores, largura, altura):
              self.frames = [RepresentacaoFrame(255) for i in range(8)]
              self.painelDePixels = painelDePixels
              self.cores = cores
              self.altura = altura
              self.largura = largura
       def gerarFrames(self):
              for linha in range(self.altura):
                     for coluna in range(self.largura):
                            if self.painelDePixels[coluna, linha] in self.cores:
                                   self.frames[linha].bits -= 2**linha
                                   print(2**linha, end='')
                            else:
                                   print(" ", end='')
                     print("\n")
       def getFrameEmBinario(self, indice):
              return bin(self.frames[indice].linhas)
       def getFramesEmBinario(self):
              return [bin(frame.linhas) for frame in self.frames]
                                   
              
              
imagem = Image.open(input("Digite o link da imagem: "))
sizeX, sizeY = imagem.size
painelDePixels = imagem.load()

if(sizeX > 8 or sizeY > 8):
       sys.exit()

gerador = GeradorDePadrao(painelDePixels, [(0,0,0,255), (0,0,0)], sizeX, sizeY)
gerador.gerarFrames()
print(gerador.getFramesEmBinario())
input("\npause")
