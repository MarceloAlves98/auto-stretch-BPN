import os
import shutil
import numpy as np

#os.system("conda activate dftbplus")
step = float(input("Quanto quer esticar a cada passo (%)? "))
lim_sup = float(input("Ate quanto (%) do tamanho original que esticar? "))
num_iteracoes = np.arange(step , (lim_sup+1) , step)
y0 = 4.5159997940

# Remover direorios (se existirem de uma run passada)

for item in num_iteracoes:
    path_name = str("/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/"+str(item)+"%")
    if os.path.isdir(path_name):
        shutil.rmtree(path_name)
        print("Apagando pasta " + str(item) + "%")
    else:
        print("Nao tem broder")

# Primeiro Passo: Rodar 0%

os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/0.0%/DOS')
os.system("./run.sh")
os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/0.0%/band')
os.system("./run.sh")

# Proximo passo: Copiar 0% e colocar (criar) o 1%

os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain')

# path to source directory
src_dir = '0.0%'

# path to destination directory
dest_dir1 = '1.0%'

# getting all the files in the source directory
#files = os.listdir(src_dir)

shutil.copytree(src_dir, dest_dir1)

os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/1.0%/DOS')

OldInput = []

# Vamos mudar o input (nao esqueca de deletar novamente os comentarios depois das linhas que 
# queremos descomentar no input original se for copiado pela primeira vez, senao vai dar aquele erro de subnodes)

with open('dftb_in.hsd' , 'r') as f:
    for line in f.readlines():
        NewLine = line.replace("\n" , "")
        OldInput.append(NewLine)

NewInput = []

for i in range(52):
    if i != 10 and i != 11:
        NewInput.append(OldInput[i])
    elif i == 10:
        NewInput.append(OldInput[10].replace("#" , ""))
    else:
        NewInput.append(OldInput[11].replace("#" , ""))

with open('dftb_in.hsd' , 'w') as g:
    for line in NewInput:
        g.write(line)
        g.write("\n")

for i in num_iteracoes:
    anterior = i - step
    atual = i
    proximo = i + step
    os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/'+str(anterior)+'%/DOS')

    OldGeo = []

    with open('geom1.out.gen' , 'r') as f:
        for line in f.readlines():
            NewLine = line.replace("\n" , " ")
            OldGeo.append(NewLine)


    # Vamos esticar a molecula

    OldY = float(OldGeo[10][24:40])
    NewY = str(round(y0 + (y0 * (i / 100)) , 9))
    NewYLine = str("   -0.8002590111E-08    " + NewY + "    0.2458364003E-10")
    print(NewY)
    print(NewYLine)
    print(type(NewYLine))

    # Temos o novo y da molecula

    # Vamos construir o novo geo.gen na pasta 1%

    os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/'+str(atual)+'%/DOS')

    NewGeo = []

    for i in range(12):
        if i != 10:
            NewGeo.append(OldGeo[i])
        else:
            NewGeo.append(NewYLine)

    with open('geo.gen' , 'w') as g:
        for line in NewGeo:
            g.write(line)
            g.write("\n")

    print(NewGeo)

    os.system("./run.sh")
    os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/'+str(atual)+'%/band')
    os.system("./run.sh")
    os.chdir('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain')

    src_dir = str(atual)+'%'
    dest_dir1 = str(proximo)+'%'

    shutil.copytree(src_dir, dest_dir1)

ultimo = lim_sup + step
shutil.rmtree('/Users/marceloalvesferreira/Desktop/recipes2/biphenylene/auto-strain/'+str(ultimo)+'%')
