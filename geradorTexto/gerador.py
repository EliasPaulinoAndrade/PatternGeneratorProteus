texto = input("Digite O Texto: ")
bits = []
for letra in texto:
    bits+="10" + format(ord(letra), "08b")[::-1] + "0"
arquivo = open("arquivo.PTN", "w")
arquivo.write(";Codigo feito por elias paulino \n0b" + ",0b".join(bits))
arquivo.close()