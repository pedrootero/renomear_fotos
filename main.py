from optparse import IndentedHelpFormatter
from posixpath import split
import os
import pandas as pd
import csv

folder = '/home/otero/projetos/rename-project/fotos/'
arquivo = open('alunos.csv')
dados = arquivo.read()
arquivo.close()

fotos = r'/home/otero/projetos/rename-project/fotos/'
file_name = os.listdir(fotos)
print(file_name)

for registro in dados.splitlines():
    nome = registro.split(',')[0]
    foto = registro.split(',')[1]
    print(nome, foto)
    if file_name == foto:
      print('Renomeando foto de', nome)
      old_name = folder + file_name
      print(old_name)
      new_name = folder + nome + '.jpg'
      print(new_name)
      os.rename(file_name, nome)

