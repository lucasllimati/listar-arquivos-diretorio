import os

pasta = 'C:/Users/lucas.lourenco/Downloads/local-manual-files'

# Somente o nome do arquivo
for arquivos in os.walk(pasta):
  for arq in arquivos:
    print(arq)

# Caminho completo
for diretorio, subspastas, arquivos in os.walk(pasta):
  for arq in arquivos:
    print(os.path.join(diretorio,arq))
