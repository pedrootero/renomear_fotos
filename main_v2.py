from optparse import IndentedHelpFormatter
from posixpath import split
import os
import pandas as pd
import csv

fotos = r'/home/otero/projetos/rename-project/fotos/'
arquivo = open('alunos.csv')
dados = arquivo.read()
arquivo.close()

file_name = os.listdir(fotos)


for registro in dados.splitlines():
    nome = registro.split(',')[0]
    foto = registro.split(',')[1]
    print(nome, foto)
    if foto in file_name:
      print('Renomeando foto de', nome)
      os.rename(fotos + foto, fotos + nome + '.jpg')
