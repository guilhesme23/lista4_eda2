import random
import math
import os
from avl import *
from plotter import plotter, tester

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
  print('1 - Criar lista aleatória')
  print('2 - Transformar lista em arvore AVL')
  print('3 - Inserir na arvore')
  print('4 - Remover da arvore')
  print('5 - Buscar na arvore')
  print('6 - Gerar grafico da inserção')
  print('7 - Gerar grafico da remoção')
  print('8 - Gerar grafico da busca')
  print('9 - Printar arvore')
  print('0 - Sair')
  option = input()
  return option

if __name__ == '__main__':
  lst = []
  exit = False
  
  while(not exit):
    option = mainMenu()
    if option == '0':
      exit =  True
      clear()
    elif option == '1':
      clear()
      entry = int(input('Insira o tamanho da lista: '))
      lst = random.sample(range(0,3*entry), entry)
      print('Lista criada com sucesso')
    elif option == '2':
      clear()
      a = AVLTree()
      for i in lst: 
        a.insert(i)
      print('Arvore criada com sucesso')  
    elif option == '3':
      clear()
      elem = int(input('Digite o elemento que deseja inserir: '))
      a.insert(elem)
      print('Elemento inserido com sucesso')
    elif option == '4':
      clear()
      x = int(input('Digite o elemento que deseja remover: '))
      a.delete(x)
      print('Elemento removido com sucesso')
    elif option == '5':
      clear()
      x = int(input('Digite o elemento que deseja procurar: '))
      exists = a.search(x)
      print('Elemento existe na arvore') if exists else print('Elemento não existe na arvore')
    elif option == '6':
      clear()
      x = int(input('Digite a quantidade de iterações: '))
      key = int(input('Digite o valor a ser inserido para o teste: '))
      times = tester(x, AVLTree.insert, a, key)
      plotter(times)
    elif option == '7':
      clear()
      x = int(input('Digite a quantidade de iterações: '))
      key = int(input('Digite o valor a ser removido para o teste: '))
      times = tester(x, AVLTree.delete, a, key)
      plotter(times)
    elif option == '8':
      clear()
      x = int(input('Digite a quantidade de iterações: '))
      key = int(input('Digite o valor a ser buscado para o teste: '))
      times = tester(x, AVLTree.search, a, key)
      plotter(times)
    elif option == '9':
      clear()
      a.display()
    else:
      pass