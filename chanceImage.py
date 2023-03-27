import os
from PIL import Image

# Definir o diretório de origem e destino
diretorio_origem = "caminho/para/o/diretorio/origem"
diretorio_destino = "caminho/para/o/diretorio/destino"

# Definir a dimensão padrão
dimensao_padrao = (800, 600)

# Loop pelos arquivos no diretório de origem
for nome_arquivo in os.listdir(diretorio_origem):
    # Verificar se o arquivo é uma imagem
    if nome_arquivo.endswith(".jpg") or nome_arquivo.endswith(".png"):
        # Abrir a imagem e redimensioná-la
        imagem = Image.open(os.path.join(diretorio_origem, nome_arquivo))
        imagem_redimensionada = imagem.resize(dimensao_padrao, Image.ANTIALIAS)
        
        # Salvar a imagem redimensionada no diretório de destino
        imagem_redimensionada.save(os.path.join(diretorio_destino, nome_arquivo))