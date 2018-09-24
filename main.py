import random
import math
import os
from avl import *

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
  print('1 - Criar lista aleatória')
  print('2 - Transformar lista em arvore AVL')
  print('3 - Inserir na arvore')
  print('4 - Remover da arvore')
  print('8 - Printar arvore')
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
    elif option == '8':
      clear()
      a.display()
    else:
      pass