import os
import shutil
import numpy as np

#os.system("conda activate dftbplus")
step = float(input("Qual step? "))
lim_sup = float(input("Ate quanto (%) do tamanho original? "))
num_iteracoes = np.arange(step , (lim_sup+1) , step)
y0 = 4.5159997940

# Remover direorios (se existirem de uma run passada)

for item in num_iteracoes:
    i = str(item)
    path_name = str("/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/"+i+"%")
    if os.path.isdir(path_name):
        shutil.rmtree(path_name)
        print("Apagando pasta " + str(item) + "%")
    else:
        print(str(item)+"% nao tem broder")