import os
import shutil
import numpy as np

#os.system("conda activate dftbplus")
step = float(input("Qual step? "))
lim_sup = float(input("Ate quanto (%) do tamanho original? "))
num_iteracoes = np.arange(step , (lim_sup+1) , step)
y0 = 4.5159997940

os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain')

# path to source directory
src_dir = '/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/0.0%'

# path to destination directory
for item in num_iteracoes:
    dest_dir = str('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/'+str(item)+'%')
    shutil.copytree(src_dir, dest_dir)