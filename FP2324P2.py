# "GO" - Segundo Projeto (FP2023)

colalfabeto = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S")

# Declaração 2.1.1
def eh_intersecao(i):
  """Verifica se um objeto é uma interseção válida.

    Args:
        i: Um objeto a ser verificado.

    Returns:
        bool: True se o objeto é uma interseção válida, False caso contrário.
  """
  # Condições a verificar
  if type(i) == tuple and len(i) == 2 and i[0] in colalfabeto and type(i[1]) == int and 1 <= i[1] <= 19 and len(i[0]) == 1:
    return True
  return False

def cria_intersecao(col, lin):
  """Cria uma interseção válida com uma coluna (letra) e linha (número) especificadas.

  Args:
      col (str): Uma letra representando a coluna.
      lin (int): Um número representando a linha.

  Returns:
      tuple: Uma interseção no formato (coluna, linha).

  Raises:
      ValueError: Se os argumentos não forem válidos.
  """
  # Verifica se os argumentos col e lin formam uma interseção válida
  if eh_intersecao((col,lin)):
     return (col,lin)
  # Surge-se erro ao inserir um argumento errado  
  raise ValueError("cria_intersecao: argumentos invalidos")

def obtem_col(i):
  """Obtém a coluna (letra) de uma interseção.

    Args:
        i (tuple): Uma interseção no formato (coluna, linha).

    Returns:
        str: A coluna da interseção.
  """
  # Retorna o primeiro elemento do tuplo 'i', que representa a coluna
  return i[0]

def obtem_lin(i):
  """Obtém a linha (número) de uma interseção.

    Args:
        i (tuple): Uma interseção no formato (coluna, linha).

    Returns:
        int: A linha da interseção.
  """
  # Retorna o segundo elemento da tupla 'i', que representa a linha
  return i[1]

def intersecoes_iguais(i1, i2):
  """Verifica se duas interseções são iguais.

  Args:
      i1 (tuple): Uma interseção no formato (coluna, linha).
      i2 (tuple): Outra interseção a ser comparada.

  Returns:
      bool: True se as interseções são iguais, False caso contrário.
  """
  # Verifica se i1 e i2 são ambas interseções válidas
  if eh_intersecao(i1) and eh_intersecao(i2):
    # Compara i1 com i2 usando "=="
    return i1 == i2
  return False

def intersecao_para_str(i):
  """Converte uma interseção em uma representação de string.

  Args:
      i (tuple): Uma interseção no formato (coluna, linha).

  Returns:
      str: Uma string representando a interseção.
  """
  # Usa f-string para criar uma string no formato "colunalinha" a partir da interseção
  return f"{obtem_col(i)}{obtem_lin(i)}"

def str_para_intersecao(s):
  """Converte uma string em uma interseção.

  Args:
      s (str): Uma string no formato 'A1'.

  Returns:
      tuple: Uma interseção no formato (coluna, linha).
  """
  # Cria uma interseção a partir da primeira letra e dos caracteres restantes.
  # A primeira letra representa a coluna, e os caracteres restantes representam a linha.
  return (s[0], int(s[1:]))

def obtem_intersecoes_adjacentes(i, l):
  """Obtém as interseções adjacentes a uma interseção em uma direção.

  Args:
      i (tuple): Uma interseção no formato (coluna, linha).
      l (tuple): A última interseção no goban.

  Returns:
      tuple: Um tuplo de interseções adjacentes na ordem 'baixo', 'esquerda', 'direita', 'cima'.
  """
  # Verifica se i e l são ambas interseções válidas
  if eh_intersecao(i) and eh_intersecao(l):
    num_colunas = colalfabeto.index(obtem_col(l))
    num_linhas = obtem_lin(l)
    poscolalfabeto = colalfabeto.index(obtem_col(i))

    intersecoes_adjacentes = []
    # Veja-se a direção "baixo"
    if obtem_lin(i) - 2 >= 0:
      intersecoes_adjacentes.append(cria_intersecao(obtem_col(i), obtem_lin(i) - 1))

    # Veja-se a direção "esquerda"
    if poscolalfabeto - 1 >= 0:
      intersecoes_adjacentes.append(cria_intersecao(colalfabeto[poscolalfabeto - 1], obtem_lin(i)))

    # Veja-se a direção "direita"
    if poscolalfabeto + 1 <= num_colunas:
      intersecoes_adjacentes.append(cria_intersecao(colalfabeto[poscolalfabeto + 1], obtem_lin(i)))

    # Veja-se a direção "cima"
    if obtem_lin(i) < num_linhas:
      intersecoes_adjacentes.append(cria_intersecao(obtem_col(i), obtem_lin(i) + 1))

    return ordena_intersecoes(intersecoes_adjacentes)

def ordena_intersecoes(intersecoes):
  """Ordena uma lista de interseções de acordo com regras específicas.

  Args:
      intersecoes (list): Uma lista de interseções.

  Returns:
      list: A lista de interseções ordenada.
  """
  # Usa a função 'sorted' para ordenar a lista de interseções com base numa chave
  # definida pela função lambda. A chave de ordenação considera primeiro o número da linha
  # e depois a coluna da interseção.
  return tuple(sorted(intersecoes, key = lambda i: (obtem_lin(i),obtem_col(i))))


# Declaração 2.1.2
def cria_pedra_branca():
  """Cria uma pedra branca.

  Returns:
      list: Uma lista representando uma pedra branca.
  """
  # Retorna uma lista contendo uma única string 'O' para representar uma pedra branca.
  return ['O']

def cria_pedra_preta():
  """Cria uma pedra preta.

  Returns:
      list: Uma lista representando uma pedra preta.
  """
  # Retorna uma lista contendo uma única string 'X' para representar uma pedra preta.
  return ['X']

def cria_pedra_neutra():
  """Cria uma pedra neutra.

  Returns:
      list: Uma lista representando uma pedra neutra.
  """
  # Retorna uma lista contendo uma única string '.' para representar uma pedra neutra.
  return ['.']

def eh_pedra(p):
  """Verifica se um objeto é uma pedra válida.

  Args:
      p: Um objeto a ser verificado.

  Returns:
      bool: True se o objeto é uma pedra válida, False caso contrário.
  """
  # Verifica se o objeto é igual a uma pedra branca, preta ou neutra
  return (p == ['O'] or p == ['X'] or p == ['.'])

def eh_pedra_branca(p):
  """Verifica se uma pedra é branca.

  Args:
      p (list): Uma lista representando uma pedra.

  Returns:
      bool: True se a pedra é branca, False caso contrário.
  """
  # Verifica se a pedra é igual a uma pedra branca
  return p == ['O']

def eh_pedra_preta(p):
  """Verifica se uma pedra é preta.

  Args:
      p (list): Uma lista representando uma pedra.

  Returns:
      bool: True se a pedra é preta, False caso contrário.
  """
  # Verifica se a pedra é igual a uma pedra preta
  return p == ['X']

def pedras_iguais(p1, p2):
  """Verifica se duas pedras são iguais.

  Args:
      p1 (list): Uma lista representando uma pedra.
      p2 (list): Outra pedra a ser comparada.

  Returns:
      bool: True se as pedras são iguais, False caso contrário.
  """
  # Verifica se p1 e p2 são ambas pedras válidas e se são iguais
  return eh_pedra(p1) and eh_pedra(p2) and p1 == p2

def pedra_para_str(p):
  """Converte uma pedra em uma representação de string ('O', 'X' ou '.').

  Args:
      p (list): Uma lista representando uma pedra.

  Returns:
      str: Uma string representando a pedra ('O', 'X' ou '.').
  """
  # Verifica se a pedra é branca, preta ou neutra e retorna a representação apropriada
  if eh_pedra_branca(p):
    return 'O'
  elif eh_pedra_preta(p):
    return 'X'
  else:
    return '.'

def eh_pedra_jogador(p):
  """Verifica se uma pedra pertence a um jogador (branco ou preto).

  Args:
      p (list): Uma lista representando uma pedra.

  Returns:
      bool: True se a pedra pertence a um jogador, False caso contrário.
  """
  # Verifica se a pedra é branca ou preta
  return (eh_pedra_branca(p) or eh_pedra_preta(p))


# Declaração 2.1.3
def cria_goban_vazio(n):
  """Cria um goban vazio com o tamanho especificado.

  Args:
      n (int): O tamanho do goban (9, 13 ou 19).

  Returns:
      dict: Um goban vazio representado como um dicionário.

  Raises:
      ValueError: Se o tamanho especificado não for válido.
  """
  # Verifica se o argumento n é um número inteiro
  if type(n) != int:
    raise ValueError("cria_goban_vazio: argumento invalido")
    
  # Verifica se o tamanho especificado está na lista de tamanhos válidos
  if n not in [9, 13, 19]:
    raise ValueError("cria_goban_vazio: argumento invalido")

  # Inicializa o goban como um dicionário
  goban = {}

  # Gera interseções para o tamanho n e preenche o goban com pedras neutras
  for col in colalfabeto[:n]:
    for lin in range(1, n + 1):
      intersecao = cria_intersecao(col, lin)
      goban[intersecao] = cria_pedra_neutra()

  return goban

def cria_goban(n, ib, ip):
  """Cria um goban com pedras brancas e pretas em posições específicas.

  Args:
      n (int): O tamanho do goban (9, 13 ou 19).
      ib (tuple): Uma tupla de interseções com pedras brancas.
      ip (tuple): Uma tupla de interseções com pedras pretas.

  Returns:
      dict: Um goban com pedras brancas e pretas nas posições especificadas.

  Raises:
      ValueError: Se os argumentos não forem válidos.
  """
  # Verifica se os argumentos n, ib e ip são do tipo correto
  if type(n) != int or type(ib) != tuple or type(ip) != tuple:
    raise ValueError("cria_goban: argumentos invalidos")

  # Verifica se o tamanho n é válido e se as interseções em ib e ip não contêm duplicados
  if n not in [9, 13, 19] or len(ib+ip) != len(list(set(ib+ip))):
    raise ValueError("cria_goban: argumentos invalidos")

  goban = cria_goban_vazio(n)
  
  # Preenche o goban com pedras brancas nas posições especificadas em ib
  for i in ib:
    if not eh_intersecao_valida(goban,i):
      raise ValueError("cria_goban: argumentos invalidos")

    if pedras_iguais(goban[i], cria_pedra_neutra()):
      goban[i] = cria_pedra_branca()
    else:
      raise ValueError("cria_goban: argumentos invalidos")
      
  # Preenche o goban com pedras pretas nas posições especificadas em ip
  for x in ip:
    if not eh_intersecao_valida(goban,x):
      raise ValueError("cria_goban: argumentos invalidos")

    if pedras_iguais(goban[x], cria_pedra_neutra()):
      goban[x] = cria_pedra_preta()
    else:
      raise ValueError("cria_goban: argumentos invalidos")

  return goban

def cria_copia_goban(t):
  """Cria uma cópia de um goban.

  Args:
      t: Um goban representado como um dicionário.

  Returns:
      dict: Uma cópia do goban.
  """
  # Inicializa um novo dicionário
  novo = {}

  # Copia os elementos do dicionário original para o novo dicionário
  for x in t.keys(): novo[x] = t[x].copy()
  return novo

def obtem_ultima_intersecao(g):
  """Obtém a última interseção no goban.

  Args:
     g (dict): Um goban representado como um dicionário.

  Returns:
      tuple: A última interseção no formato (coluna, linha).
  """
  maior_lin_index = -1
  maior_col_index = -1

  for intersecao in g:
    linha = obtem_lin(intersecao)
    coluna = colalfabeto.index(obtem_col(intersecao))

    if linha > maior_lin_index:
      maior_lin_index = linha

    if coluna > maior_col_index:
      maior_col_index = coluna
      
  # Cria e retorna a última interseção com base nos índices encontrados
  return cria_intersecao(colalfabeto[maior_col_index], maior_lin_index)

def obtem_pedra(g, i):
  """Obtém a pedra em uma interseção específica no goban.

  Args:
      g (dict): Um goban representado como um dicionário.
      i (tuple): Uma interseção no formato (coluna, linha).

  Returns:
      list: Uma lista representando a pedra na interseção.
  """
  # Retorna a pedra na interseção específica i no goban g
  return g[i]

def obtem_cadeia(goban, intersecao):
  """Obtém a cadeia de pedras conectadas em uma interseção.

  Args:
      goban (dict): Um goban representado como um dicionário.
      intersecao (tuple): Uma interseção no formato (coluna, linha).

  Returns:
      list: Uma lista de interseções representando a cadeia.
  """
  tipo_pedra = obtem_pedra(goban, intersecao)
  cadeia, to_check = [], [intersecao]

  while to_check:
    intersecao_atual = to_check.pop()
    cadeia.append(intersecao_atual)

    for adjacente in obtem_intersecoes_adjacentes(intersecao_atual, obtem_ultima_intersecao(goban)):
      if pedras_iguais(obtem_pedra(goban, adjacente), tipo_pedra) and adjacente not in cadeia and adjacente not in to_check:
        to_check.append(adjacente)

  return tuple(ordena_intersecoes(cadeia))

def coloca_pedra(g, i, p):
  """Coloca uma pedra em uma interseção específica no goban.

  Args:
      g (dict): Um goban representado como um dicionário.
      i (tuple): Uma interseção no formato (coluna, linha).
      p (list): Uma lista representando a pedra a ser colocada.

  Returns:
      dict: O goban atualizado após a colocação da pedra.
  """
  # Coloca a pedra na interseção específica i no goban g
  g[i] = p
  return g

def remove_pedra(g, i):
  """Remove uma pedra de uma interseção específica no goban.

  Args:
      g (dict): Um goban representado como um dicionário.
      i (tuple): Uma interseção no formato (coluna, linha).

  Returns:
      dict: O goban atualizado após a remoção da pedra.
  """
  # Coloca uma pedra neutra na interseção específica i para remover a pedra
  g = coloca_pedra(g,i,cria_pedra_neutra())
  return g

def remove_cadeia(g, t):
  """Remove uma cadeia de pedras do goban.

  Args:
      g (dict): Um goban representado como um dicionário.
      t (list): Uma lista de interseções representando a cadeia a ser removida.

  Returns:
      dict: O goban atualizado após a remoção da cadeia.
  """
  for i in t:
    remove_pedra(g,i)

  return g

def eh_goban(g):
  """Verifica se um objeto é um goban válido.

  Args:
      g: Um objeto a ser verificado.

  Returns:
      bool: True se o objeto é um goban válido, False caso contrário.
  """

  if type(g) != dict or len(g) not in [9**2,13**2,19**2]:
    return False

  for intersecao in g:
    if not eh_intersecao(intersecao):
      return False

    if not eh_pedra(g[intersecao]):
      return False

  return True

def eh_intersecao_valida(g, i):
  """Verifica se uma interseção é válida em um goban.

  Args:
      g (dict): Um goban representado como um dicionário.
      i (tuple): Uma interseção no formato (coluna, linha).

  Returns:
      bool: True se a interseção é válida no goban, False caso contrário.
  """
  return eh_intersecao(i) and i in g

def eh_str_valida(s):
  """Verifica se uma string é válida no formato 'A1' a 'T19'.

  Args:
      s (str): Uma string a ser verificada.

  Returns:
      bool: True se a string é válida, False caso contrário.
  """
  return type(s) == str and 2 <= len(s) <= 3 and s[0] in colalfabeto and s[1:].isdigit()

def gobans_iguais(g1, g2):
  """Verifica se dois gobans são iguais.

  Args:
      g1 (dict): Um goban representado como um dicionário.
      g2 (dict): Outro goban a ser comparado.

  Returns:
      bool: True se os gobans são iguais, False caso contrário.
  """
  tamanho1 = obtem_lin(obtem_ultima_intersecao(g1))
  tamanho2 = obtem_lin(obtem_ultima_intersecao(g2))

  if tamanho1 != tamanho2:
    return False

  for i in range(tamanho1):
    for x in range(tamanho2):
      inter = cria_intersecao(colalfabeto[i],x+1)
      if not pedras_iguais(obtem_pedra(g1,inter), obtem_pedra(g2,inter)):
        return False
        # Compara as pedras nas interseções dos dois gobans e retorna False se forem diferentes

  return True

def goban_para_str(goban):
  """Converte um goban em uma representação de string.

    Args:
        goban (dict): Um goban representado como um dicionário.

    Returns:
        str: Uma string representando o goban.
    """
  terr_str = ""
  num_colunas = colalfabeto.index(obtem_col(obtem_ultima_intersecao(goban))) + 1
  terr_str += "   " + " ".join(colalfabeto[:num_colunas]) + "\n"
  num_linhas = obtem_lin(obtem_ultima_intersecao(goban))

  for i in reversed(range(1, num_linhas + 1)):
    linha = f"{i:2d}"

    for j in range(num_colunas):
      intersecao = cria_intersecao(colalfabeto[j], i)
      if intersecao in goban:
        tipo_pedra = obtem_pedra(goban, intersecao)
        if eh_pedra_branca(tipo_pedra):
          linha += " O" # Adiciona 'O' para pedra branca
        elif eh_pedra_preta(tipo_pedra):
          linha += " X" # Adiciona 'X' para pedra preta
        else:
          linha += " ." # Adiciona '.' para pedra neutra
      else:
        linha += " ."

    linha += f" {i:2d}\n"
    terr_str += linha

  terr_str += "   " + " ".join(colalfabeto[:num_colunas])

  return terr_str

def obtem_territorios(goban):
  """Obtém e ordena os territórios no goban.

  Args:
      goban (dict): Um goban representado como um dicionário.

  Returns:
      tuple: Um tuplo de listas de interseções representando os territórios.
  """
  territorios = []
  lado = obtem_lin(obtem_ultima_intersecao(goban))
  for i in range(lado):
    for j in range(lado):
      intersecao = cria_intersecao(colalfabeto[i],j+1)
      pedra = obtem_pedra(goban,intersecao)
  
      if pedras_iguais(pedra, cria_pedra_neutra()):
        territorio_existente = False
        for territorio in territorios:
          if intersecao in territorio:
            territorio_existente = True
            break
        if not territorio_existente:
          territorios.append(obtem_cadeia(goban, intersecao))

  # Ordenar os territórios
  territorios = sorted(territorios, key=lambda x: (obtem_lin(x[0]), obtem_col(x[0])))
  return tuple(territorios)

def obtem_adjacentes_diferentes(goban, territorio):
  """Obtém as interseções adjacentes a um território com pedras de jogadores diferentes.

  Args:
      goban (dict): Um goban representado como um dicionário.
      territorio (tuple): Uma tupla de interseções representando um território.

  Returns:
      tuple: Um tuplo de interseções adjacentes a jogadores de cores diferentes.
  """
  ultima_intersecao = obtem_ultima_intersecao(goban)
  intersecoes_adjacentes = []

  for intersecao in territorio:
    adjacentes = obtem_intersecoes_adjacentes(intersecao, ultima_intersecao)
    for adjacente in adjacentes:
      if adjacente not in intersecoes_adjacentes and eh_pedra_jogador(obtem_pedra(goban,adjacente)) != eh_pedra_jogador(obtem_pedra(goban,intersecao)):
        intersecoes_adjacentes.append(adjacente)

  return ordena_intersecoes(intersecoes_adjacentes)

def jogada(g, i, p):
  """Realiza uma jogada no goban, colocando uma pedra em uma interseção.

  Args:
      g (dict): Um goban representado como um dicionário.
      i (tuple): Uma interseção no formato (coluna, linha).
      p (list): Uma lista representando a pedra a ser colocada.

  Returns:
      dict: O goban atualizado após a jogada.
  """
  g = coloca_pedra(g, i, p)

  intersecoes_adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))

  for intersecao_adjacente in intersecoes_adjacentes:
    if eh_pedra_jogador(obtem_pedra(g,intersecao_adjacente)) and not pedras_iguais(p,obtem_pedra(g,intersecao_adjacente)):
      cadeia = obtem_cadeia(g, intersecao_adjacente)
      if len(obtem_adjacentes_diferentes(g, cadeia)) == 0:
        g = remove_cadeia(g, cadeia)

  return g

def obtem_pedras_jogadores(g):
  """Conta o número de pedras brancas e pretas no goban.

  Args:
      g (dict): Um goban representado como um dicionário.

  Returns:
      tuple: Um tuplo com a contagem de pedras brancas e pretas.
  """
  counter_brancas = 0
  counter_pretas = 0

  lado = obtem_lin(obtem_ultima_intersecao(g))
  for i in range(lado):
    for j in range(lado):
      intersecao = cria_intersecao(colalfabeto[i],j+1)
      if eh_pedra_preta(obtem_pedra(g,intersecao)):
        counter_pretas += 1
      elif eh_pedra_branca(obtem_pedra(g,intersecao)):
        counter_brancas += 1

  return (counter_brancas, counter_pretas)


# Declaração de 2.2.1
def calcula_pontos(g):
  """Calcula os pontos para os jogadores com base no estado atual do goban.

  Args:
      g (dict): Um goban representado como um dicionário.

  Returns:
      tuple: Um tuplo com os pontos para os jogadores brancos e pretos.
  """
  pontos_brancos, pontos_pretos = obtem_pedras_jogadores(g)
  territorios = obtem_territorios(g)

  for territorio in territorios:
    fronteira = []

    for adjacente in obtem_adjacentes_diferentes(g, territorio):
      fronteira.append(eh_pedra_branca(obtem_pedra(g, adjacente)))

    if all(fronteira) and len(fronteira) > 0:
      pontos_brancos += len(territorio)
    elif not any(fronteira) and len(fronteira) > 0:
      pontos_pretos += len(territorio)

  return (pontos_brancos, pontos_pretos)


# Declaração de 2.2.2
def eh_jogada_legal(goban, intersecao, pedra, l):
  """Verifica se uma jogada é legal de acordo com as regras do jogo.

  Args:
      goban (dict): Um goban representado como um dicionário.
      intersecao (tuple): Uma interseção no formato (coluna, linha).
      pedra (list): Uma lista representando a pedra a ser colocada.
      l (tuple): A última interseção no goban.

  Returns:
      bool: True se a jogada é legal, False caso contrário.
  """
  def tem_liberdade(goban,intersecao):
    c = obtem_cadeia(goban,intersecao)
    if any(not eh_pedra_jogador(obtem_pedra(goban,j)) for j in obtem_adjacentes_diferentes(goban,c)):
      return True
    return False

  copia = cria_copia_goban(goban)

  if not eh_intersecao_valida(goban,intersecao) or eh_pedra_jogador(obtem_pedra(goban, intersecao)):
    return False

  jogada(copia,intersecao,pedra)

  if not tem_liberdade(copia,intersecao):
    return False

  if gobans_iguais(copia,l):
    return False
  return True


# Declaração de 2.2.3
def turno_jogador(g, p, l):
  """Realiza o turno de um jogador, permitindo que ele faça uma jogada no goban.

  Args:
      g (dict): Um goban representado como um dicionário.
      p (list): Uma lista representando a pedra do jogador.
      l (tuple): A última interseção no goban.

  Returns:
      bool: True se o jogador fez uma jogada válida, False se o jogador passou.

  A função solicita ao jogador uma jogada, verifica se a jogada é válida e a aplica ao goban.
  Caso o jogador opte por passar, a função retorna False. Caso contrário, se o jogador
  fizer uma jogada válida, a função retorna True.
  """
  while True:
    resposta = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(p)}]:")
  
    if resposta == "P":
      return False
  
    if eh_str_valida(resposta) and eh_intersecao_valida(g, str_para_intersecao(resposta)) and eh_jogada_legal(g, str_para_intersecao(resposta), p, l):
        g = jogada(g, str_para_intersecao(resposta), p)
        return True


# Declaração de 2.2.4
def go(n, tb, tp):
  """
  Função principal do jogo Go.

  Args:
      n (int): O tamanho do goban (9, 13 ou 19).
      tb (tuple): Uma tupla de interseções com pedras brancas.
      tp (tuple): Uma tupla de interseções com pedras pretas.

  Returns:
      bool: True se o jogador branco vencer, False caso contrário.

  Raises:
      ValueError: Se os argumentos não forem válidos.
  """
  # Inicializa as variáveis de controle para os jogadores branco e preto
  branco = True
  preto = True

  # Inicializa as listas de interseções para as pedras brancas e pretas
  tb_intersecoes = ()
  tp_intersecoes = ()

  # Valida os argumentos de entrada
  if n not in [9, 13, 19] or type(tb) != tuple or type(tp) != tuple or len(tb+tp) != len(list(set(tb+tp))):
    raise ValueError('go: argumentos invalidos')

  # Cria um goban vazio com o tamanho especificado
  goban = cria_goban_vazio(n)

  # Valida e converte as interseções fornecidas em argumentos para o formato de interseções válidas
  for x in tb + tp:
    if not eh_str_valida(x) or not eh_intersecao_valida(goban,str_para_intersecao(x)):
      raise ValueError("go: argumentos invalidos")

  # Converte as interseções fornecidas em argumentos para o formato de interseções válidas
  for x in tb:
    tb_intersecoes += (str_para_intersecao(x),)

  for x in tp:
    tp_intersecoes += (str_para_intersecao(x),)
  
  goban = cria_goban(n, tb_intersecoes, tp_intersecoes)
  pedra = cria_pedra_preta()

   # Inicializa cópias dos estados anteriores do goban para ambos os jogadores
  anterior_preto = cria_copia_goban(goban)
  anterior_branco = cria_copia_goban(goban)

  while preto or branco:
    pontos = calcula_pontos(goban)
    print(f'Branco (O) tem {pontos[0]} pontos')
    print(f'Preto (X) tem {pontos[1]} pontos')
    print(goban_para_str(goban))
    # Chama a função de turno_jogador para permitir que o jogador faça uma jogada
    if turno_jogador(goban,pedra,anterior_preto if eh_pedra_preta(pedra) else anterior_branco):
      if eh_pedra_preta(pedra):
        anterior_preto = cria_copia_goban(goban)
        preto = True
        pedra = cria_pedra_branca()
      else:
        anterior_branco = cria_copia_goban(goban)
        branco = True
        pedra = cria_pedra_preta()
    else:
      if eh_pedra_preta(pedra):
        preto = False
        pedra = cria_pedra_branca()
      else:
        branco = False
        pedra = cria_pedra_preta()

  pontos = calcula_pontos(goban)
  print(f'Branco (O) tem {pontos[0]} pontos')
  print(f'Preto (X) tem {pontos[1]} pontos')
  print(goban_para_str(goban))

  return pontos[0] >= pontos[1]