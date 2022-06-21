'''
Universidade Federal de Roraima
Data: 05/06/2022
Aluna: Wandressa Reis 
Matrícula: 2020014698
Turma: Ciência da Computação 2020.2
Professor: Acauan


4) Tendo como base o algoritmo de árvore binária de busca visto em sala, 
implemente os seguintes métodos:
- altura() : retorna a altura tendo como base o nó passado como referencia
- minimo() : retornar o menor valor da arvore
- maximo() : retornar o maior valor da arvore
- remocao() : implemente um método que remova um elemento passado como 
parâmetro

'''

### ----- ÁRVORE DE BUSCA BINÁRIA  ----- ###


# Estrutura do nó
class No:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

def inserirNo(root, value):
  if root is None:
    return No(value)
  else:
    if value < root.value:
      root.left = inserirNo(root.left, value)
    elif value > root.value:
      root.right = inserirNo(root.right, value)
  return root 
  

# PERCURSOS EM PROFUNDIDADE (DFS)
def preOrdem(root):
  if root:
    print(root.value, end=" ")
    preOrdem(root.left)
    preOrdem(root.right)

def emOrdem(root):
  if root:
    emOrdem(root.left)
    print(root.value, end=" ")
    emOrdem(root.right)

def posOrdem(root):
  if root:
    posOrdem(root.left)
    posOrdem(root.right)
    print(root.value, end=" ")
    

# Função print

def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level+1)
    print(' ' *4*level + '->' +str(root.value))
    printTree(root.left, level+1)

# FUNÇÃO PARA VERIFICAR A ALTURA

def altura(root):
  if root is None:
    return -1
  leftH = altura(root.left)

# FUNÇÃO PARA VERIFICAR O VALOR MÍNIMO

def minimo(root):
  if root is None:
    return None
  while root.left != None:
    root = root.left
  return root

# FUNÇÃO PARA VERIFICAR O VALOR MÁXIMO
  
def maximo(root):
  if root is None:
    return None
  while root.right != None:
    root = root.right
  return root

# FUNÇÃO DE REMOÇÃO

def remocao(root, value):
  if root is None: return None
  elif value < root.value:
    root.left = remocao(root.left, value)
  elif value > root.value:
    root.right = remocao(root.right, value)
  else: # Nó foi encontrado
    # Caso 1: Nó folha
    if root.left and root.right is None: 
      root = None 
    # Caso 2: Nó tem um filho 
    elif root.left is None:
      temp = root 
      root = root.right
      temp = None
      return root
    elif root.right is None: 
      temp = root 
      root = root.left
      temp = None
    # Caso 3: Nó tem dois filhos 
    else: 
      noMinimo = minimo(root.right)
      root.value = noMinimo.value
      root.right = remocao(root.right, noMinimo.value)
  return root 

   
# ------ Main --------
root = None

root = inserirNo(root, 10)
root = inserirNo(root, 5)
root = inserirNo(root, 2)
root = inserirNo(root, 35)
root = inserirNo(root, 8)
root = inserirNo(root, 40)
root = inserirNo(root, 38)
root = inserirNo(root, 51)
root = inserirNo(root, 35)
root = inserirNo(root, 9)

printTree(root)
print("Altura: ", altura(root))
print("Míninmo: ", minimo(root).value)
print("Máximo: ", maximo(root).value)
print('Remoção do número 10:')
remocao(root, 10)
printTree(root)