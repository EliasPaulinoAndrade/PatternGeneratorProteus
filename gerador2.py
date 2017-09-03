import os, sys
from PIL import Image

class RepresentacaoFrame:
       def __init__(self, bitsLinhas, bitsColuns):
              self.bitsLinhas = bitsLinhas
              self.bitsColuns = bitsColuns
class GeradorDePadrao:
       def __init__(self, painelDePixels, cores, largura, altura):
              self.frames = [RepresentacaoFrame(255, 0) for i in range(8)]
              self.painelDePixels = painelDePixels
              self.rotacoes = []
              self.cores = cores
              self.altura = altura
              self.largura = largura
       def gerarFrames(self):
              for linha in range(self.altura):
                     entrou = False
                     for coluna in range(self.largura):
                            if self.painelDePixels[coluna, linha] in self.cores:
                                   self.frames[coluna].bitsLinhas -= 2**linha
              for coluna in range(self.largura):
                     self.frames[coluna].bitsColuns += 2**coluna
       def getFramesLinhasEmBinario(self):
              return [bin(frame.bitsLinhas) for frame in self.frames]
       def getFramesColunasEmBinario(self):
              return [bin(frame.bitsColuns) for frame in self.frames]
       def gerarRotacoes(self):
              framesAtual = self.frames[:]
              self.rotacoes = []
              frameAux = None
              for frame in framesAtual:
                      frameAux = framesAtual.pop()
                      framesAtual.insert(0, frameAux)
                      self.rotacoes.append(framesAtual[:])
       def getRotacoesLinhasEmBinario(self):
              ar = []
              for frames in self.rotacoes:
                      ar += [bin(frame.bitsLinhas) for frame in frames]
              return ar
       def getRotacoesColunasEmBinario(self):
              ar = []
              for frames in self.rotacoes:
                      ar += [bin(frame.bitsColuns) for frame in frames]
              return ar
     
              
imagens = int(input("QuantasImagens ?"))
for i in range(imagens):
    imagem = Image.open(input("Digite o link da imagem: "))
    sizeX, sizeY = imagem.size
    painelDePixels = imagem.load()

    if(sizeX > 8 or sizeY > 8):
        sys.exit()

    gerador = GeradorDePadrao(painelDePixels, [(0,0,0,255), (0,0,0)], sizeX, sizeY)
    gerador.gerarFrames()
    print(' ,'.join(gerador.getFramesLinhasEmBinario()))
    print(' ,'.join(gerador.getFramesColunasEmBinario()))