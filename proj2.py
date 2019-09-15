# Nome: Pedro Manuel Fernandez Godinho  Numero: 93608
def cria_celula(n):
    """Uma funcao que recebe o valor do estado de uma celula e devolve uma celula com esse valor.

    O tipo celula e representado internamente como uma lista com um inteiro que pode ter o valor -1, 0 ou 1
    As funcoes modificadoras sobre celulas sao, portanto, destrutivas.

    Args:
        n (int): O valor da celula. Tem de pertencer a [-1, 1]

    Returns:
        celula: A celula com o valor recebido

    Raises:
        ValueError: Se o valor nao for um inteiro em [-1, 1]
    """
    if not (isinstance(n, int) and -1 <= n <= 1):
        raise ValueError('cria_celula: argumento invalido.')
    return [n]


def obter_valor(cell):
    """Uma funcao que retorna o valor da celula na forma de um inteiro.
    Nao realiza verificacao de argumentos.

    Args:
        cell (celula): A celula a ler

    Returns:
        int: O valor da celula
    """
    return cell[0]


def inverte_estado(cell):
    """Uma funcao retorna a celula inversa da celula recebida caso o valor desta nao seja incerto.
    Nao realiza verificacao de argumentos.

    Args:
        cell (celula): A celula a inverter

    Returns:
        celula: A celula invertida
    """
    if cell[0] == 1:
        cell[0] = 0
    elif cell[0] == 0:
        cell[0] = 1
    return cell


def eh_celula(cell):
    """Uma funcao que verifica se o argumento e uma celula.

    Args:
         cell (universal): O tipo a verificar se e uma celula

    Returns:
        bool: True se o argumento for uma celula, False se nao
    """
    return isinstance(cell, list) and len(cell) == 1 and isinstance(cell[0], int) and cell[0] in [-1, 0, 1]


def celulas_iguais(c1, c2):
    """Uma funcao que verifica a igualdade entre duas celulas.
    Nao realiza verificacao de argumentos.

    Args:
        c1 (celula): A primeica celula
        c2 (celula): A segunda celula

    Returns:
        bool: Verdadeiro se forem celulas iguais, False se nao.
    """
    return eh_celula(c1) and eh_celula(c2) and c1 == c2


def celula_para_str(cell):
    """Uma funcao que retorna a representacao da celula como str.
    Nao realiza verificacao de argumentos.

    Args:
         cell (celula): A celula cuja representacao retornar

    Returns:
        str: A representacao do argumento
    """
    if cell[0] == -1:
        return 'x'
    return str(cell[0])


def cria_coordenada(r, c):
    """Uma funcao que retorna a coordenada de uma celula com a linha l e a coluna c.

    O tipo coordenada e representado internamente por um tuplo de dois elementos, a colune e a linha.
    Nao existem funcoes destrutivas sobre coordenadas.

    Args:
        l (int): Um natural relativo a linha da coordenada
        c (int): Um natural relativo a coluna da coordenada

    Returns:
        coordenada: A coordenada com a linha e coluna recebidas

    Raises:
        ValueError: Caso os argumentos nao sejam inteiros maiores que 0
    """
    if not (isinstance(r, int) and isinstance(c, int) and 0 <= r <= 2 and 0 <= c <= 2):
        raise ValueError('cria_coordenada: argumentos invalidos.')
    return r, c


def coordenada_linha(coord):
    """Uma funcao que retorna a linha da coordenada recebida.
    Nao realiza verificacao de argumentos.

    Args:
        coord (coordenada): A coordenada a ler

    Returns:
        int: a linha da coordenada
    """
    return coord[0]


def coordenada_coluna(coord):
    """Uma funcao que retorna a coluna da coordenada recebida.
    Nao realiza verificacao de argumentos.

    Args:
        coord (coordenada): A coordenada a ler

    Returns:
        int: a coluna da coordenada
    """
    return coord[1]


def eh_coordenada(coord):
    """Uma funcao que verifica se o seu argumento e uma coordenada.

    Args:
        coord (universal): O tipo a verificar se e uma coordenada

    Returns:
        bool: True se for uma coordenada, nao se nao for
    """
    return isinstance(coord, tuple) and len(coord) == 2 and \
           isinstance(coord[0], int) and isinstance(coord[1], int) and \
           0 <= coord[0] <= 2 and 0 <= coord[1] <= 2


def coordenadas_iguais(c1, c2):
    """Uma funcao que verifica se duas coordenadas sao iguais.
    Nao realiza verificacao de argumentos.

    Args:
        c1 (coordenada): A primeira coordenada
        c2 (coordenada): A segunda coordenada

    Returns:
        bool: True se forem iguais, nao se nao forem
    """
    # A igualdade entre tuplos no python verifica cada elemento com o elemento do mesmo indice no outro tuplo,
    # comparando as coordenadas do modo esperado para o contexto do problema
    return c1 == c2


def coordenada_para_str(coord):
    """Uma funcao que retorna a representacao da coordenada como string.
    Nao realiza verificacao de argumentos.

    Args:
        coord (coordenada): A coordenada a representar

    Returns:
        str: A representacao da coordenada
    """
    return '({}, {})'.format(coord[0], coord[1])


def tabuleiro_inicial():
    """Uma funcao que retorna o tabuleiro inicial do jogo.
    Um tabuleiro e uma matrix de 3x3 na qual a coordenada (2,0) nao existe.

    O tipo tabuleioro e representado internamente por um dicionario com coordenadas como keys e celulas como values.
    Note-se as funcoes sobre tabuleiros sao destrutivas.

    Returns:
        tabuleiro: O tabuleiro inicial
    """
    return {cria_coordenada(0, 0): cria_celula(-1),
            cria_coordenada(0, 1): cria_celula(-1),
            cria_coordenada(0, 2): cria_celula(-1),
            cria_coordenada(1, 0): cria_celula(0),
            cria_coordenada(1, 1): cria_celula(0),
            cria_coordenada(1, 2): cria_celula(-1),
            cria_coordenada(2, 1): cria_celula(0),
            cria_coordenada(2, 2): cria_celula(-1)}


def str_para_tabuleiro(s):
    """Uma funcao que retorna o tabuleiro correspondente a string recebida.

    Args:
        s (str): A representacao em string do tabuleiro como tuplo de 3 tuplos, como no projeto 1

    Returns:
        tabuleiro: O tabuleiro que a string representa

    Raises:
        ValueError: Caso o argumento nao seja uma string que coincida com o formato esperado.
    """
    if not isinstance(s, str):
        raise ValueError('str_para_tabuleiro: argumento invalido.')

    nums = eval(s)

    if not (isinstance(nums, tuple) and len(nums) == 3 and
            all(isinstance(line, tuple) and all(isinstance(cell, int) for cell in line) for line in nums)):
        raise ValueError('str_para_tabuleiro: argumento invalido.')

    return {cria_coordenada(0, 0): cria_celula(nums[0][0]),
            cria_coordenada(0, 1): cria_celula(nums[0][1]),
            cria_coordenada(0, 2): cria_celula(nums[0][2]),
            cria_coordenada(1, 0): cria_celula(nums[1][0]),
            cria_coordenada(1, 1): cria_celula(nums[1][1]),
            cria_coordenada(1, 2): cria_celula(nums[1][2]),
            cria_coordenada(2, 1): cria_celula(nums[2][0]),
            cria_coordenada(2, 2): cria_celula(nums[2][1])}


def tabuleiro_dimensao(tab):
    """Uma funcao que retorna a dimensao do tabuleiro.
    Nao realiza verificacao de argumentos.

    Args:
        tab (tabuleiro): O tabuleiro a verificar

    Returns:
        int: A dimensao do tabuleiro
    """
    dim = 0
    for coord in tab:
        dim = max(dim, coordenada_linha(coord))

    return dim + 1


def tabuleiro_celula(tab, coord):
    """Uma funcao que retorna a celula correspondente a uma certa coordenada do tabuleiro.

    Args:
        tab (tabuleiro): O tabuleiro do qual ler a celula
        coord (coordenada): A coordenada do qual ler a celula

    Returns:
        celula: A celula na coordenada recebida
    """
    return tab[coord]


def tabuleiro_substitui_celula(tab, cell, coord):
    """Uma funcao que subsitui a celula na coordenada do tabuleiro por outra.
    Esta funcao e destrutiva.

    Args:
        tab (tabuleiro): O tabuleiro a mudar
        cell (celula): A celula a inserir no tabuleiro
        coord (coordenada): A coordenada onde colocar a celula

    Returns:
        tabuleiro: O tabuleiro modificado

    Raises:
        ValueError: Caso a coordenada nao seja valida para um tabuleiro 3x3
    """
    if (not (eh_tabuleiro(tab) and eh_coordenada(coord))) or coordenadas_iguais(coord, cria_coordenada(2, 0)):
        raise ValueError('tabuleiro_celula: argumentos invalidos.')
    tab[coord] = cell
    return tab


def tabuleiro_inverte_estado(tab, coord):
    """Uma funcao que inverte o valor de uma celula do tabuleiro.
    Esta funcao e destrutiva.

    Args:
        tab (tabuleiro): O tabuleiro a mudar
        coord (coordenada): A coordenada cuja celula inverter

    Returns:
        tabuleiro: O tabuleiro modificado

    Raises:
        ValueError: Caso a coordenada nao seja valida para um tabuleiro 3x3
    """
    if (not (eh_tabuleiro(tab) and eh_coordenada(coord))) or coordenadas_iguais(coord, cria_coordenada(2, 0)):
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')
    tab[coord] = inverte_estado(tab[coord])
    return tab


def eh_tabuleiro(tab):
    """Uma funcao que verifica se o seu argumento e um tabuleiro.

    Args:
        tab (universal): O tipo a verificar se e um tabuleiro

    Returns:
        bool: True se o argumento for um tabuleiro, False se nao o for
    """
    if not (isinstance(tab, dict) and len(tab) == 8):
        return False
    for r in range(3):
        for c in range(3):
            if r != 2 or c != 0:
                if not (cria_coordenada(r, c) in tab):
                    return False
                e = tab[cria_coordenada(r, c)]
                if not eh_celula(e):
                    return False
    return True


def tabuleiros_iguais(t1, t2):
    """Uma funcao que verifica a igualdade entre dois tabuleiros.
    Nao realiza verificacao de argumentos.

    Args:
        t1 (tabuleiro): O primeiro tabuleiro
        t2 (tabuleiro): O segundo tabuleiro

    Returns:
        bool: True se os tabuleiros forem iguais, False se nao forem
    """
    # A igualdade entre dicionarios em python verifica se para cada par key-value num dicionario, existe um par com a
    # mesma key e o mesmo value no outro, comparando corretamente os tabuleiros.
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


def tabuleiro_para_str(tab):
    """Uma funcao que retorna a representacao em string do tabuleiro recebido.
    Nao realiza verificacao de argumentos.

    Args:
        tab (tabuleiro): O tabuleiro a representar

    Returns:
        str: A representacao do tabuleiro.
    """
    s = '+-------+\n'
    s += '|...{}...|\n'.format(celula_para_str(tab[cria_coordenada(0, 2)]))
    s += '|..{}.{}..|\n'.format(celula_para_str(tab[cria_coordenada(0, 1)]),
                                celula_para_str(tab[cria_coordenada(1, 2)]))
    s += '|.{}.{}.{}.|\n'.format(celula_para_str(tab[cria_coordenada(0, 0)]),
                                 celula_para_str(tab[cria_coordenada(1, 1)]),
                                 celula_para_str(tab[cria_coordenada(2, 2)]))
    s += '|..{}.{}..|\n'.format(celula_para_str(tab[cria_coordenada(1, 0)]),
                                celula_para_str(tab[cria_coordenada(2, 1)]))
    s += '+-------+'
    return s


def porta_xz(tab, prt, ld):
    """Uma funcao que aplica de forma destrutiva a porta X ou Z num tabuleiro.

    Args:
        tab (tabuleiro): O tabuleiro sobre o qual realizar a porta
        prt (str): A porta a realizar ('X' ou 'Z')
        ld (str): O lado sobre o qual realizar a porta ('E' ou 'D')

    Returns:
        tabuleiro: O tabuleiro depois da porta ser aplicada

    Raises:
        ValueError: Caso um dos argumentos seja invalido
    """
    if not (eh_tabuleiro(tab) and
            isinstance(ld, str) and ld in ('E', 'D') and
            isinstance(prt, str) and prt in ('X', 'Z')):
        raise ValueError('porta_xz: argumentos invalidos.')
    # Se a porta for Z a linha e coluna a mudar para o lado esquerdo ou direiro sao 0 e 2
    esq = 0
    drt = 2
    # Se a porta for X a linha e coluna a mudar para o lado esquerdo ou direito sao 1 e 1
    if prt == 'X':
        esq = 1
        drt = 1

    if ld == 'E':
        tabuleiro_inverte_estado(tab, cria_coordenada(esq, 0))
        tabuleiro_inverte_estado(tab, cria_coordenada(esq, 1))
        tabuleiro_inverte_estado(tab, cria_coordenada(esq, 2))
    else:
        tabuleiro_inverte_estado(tab, cria_coordenada(0, drt))
        tabuleiro_inverte_estado(tab, cria_coordenada(1, drt))
        tabuleiro_inverte_estado(tab, cria_coordenada(2, drt))

    return tab


def porta_x(tab, ld):
    """Uma funcao que aplica de forma destrutiva a porta X num tabuleiro.

    Args:
        tab (tabuleiro): O tabuleiro sobre o qual realizar a porta
        ld (str): O lado sobre o qual realizar a porta ('E' ou 'D')

    Returns:
        tabuleiro: O tabuleiro depois da porta ser aplicada

    Raises:
        ValueError: Caso um dos argumentos seja invalido
    """
    if not (eh_tabuleiro(tab) and isinstance(ld, str) and ld in ('E', 'D')):
        raise ValueError('porta_x: argumentos invalidos.')
    return porta_xz(tab, 'X', ld)


def porta_z(tab, ld):
    """Uma funcao que aplica de forma destrutiva a porta Z num tabuleiro.

    Args:
        tab (tabuleiro): O tabuleiro sobre o qual realizar a porta
        ld (str): O lado sobre o qual realizar a porta ('E' ou 'D')

    Returns:
        tabuleiro: O tabuleiro depois da porta ser aplicada

    Raises:
        ValueError: Caso um dos argumentos seja invalido
    """
    if not (eh_tabuleiro(tab) and isinstance(ld, str) and ld in ('E', 'D')):
        raise ValueError('porta_z: argumentos invalidos.')
    return porta_xz(tab, 'Z', ld)


def tabuleiro_troca_celulas(tab, coord1, coord2):
    """Uma funcao que troca o valor de duas celulas do tabuleiro.
    Esta funcao e destrutiva.

    Args:
        tab (tabuleiro): O tabuleiro a mudar
        coord1 (coordenada): A primeira coordenada a trocar
        coord2 (coordenada): A segunda coordenada a trocar

    Returns:
        tabuleiro: O tabuleiro modificado

    Raises:
        ValueError: Caso alguma das coordenadas nao seja valida para um tabuleiro 3x3
    """
    if (not (eh_tabuleiro(tab)) and eh_coordenada(coord1) and eh_coordenada(coord2)) or \
            coordenadas_iguais(coord1, cria_coordenada(2, 0)) or coordenadas_iguais(coord2, cria_coordenada(2, 0)):
        raise ValueError('tabuleiro_troca_celulas: argumentos invalidos.')
    celula_temp = tabuleiro_celula(tab, coord2)
    tabuleiro_substitui_celula(tab, tabuleiro_celula(tab, coord1), coord2)
    tabuleiro_substitui_celula(tab, celula_temp, coord1)
    return tab


def porta_h(tab, ld):
    """Uma funcao que aplica de forma destrutiva a porta H num tabuleiro.

    Args:
        tab (tabuleiro): O tabuleiro sobre o qual realizar a porta
        ld (str): O lado sobre o qual realizar a porta ('E' ou 'D')

    Returns:
        tabuleiro: O tabuleiro depois da porta ser aplicada

    Raises:
        ValueError: Caso um dos argumentos seja invalido
    """
    if not (eh_tabuleiro(tab) and isinstance(ld, str) and ld in ('E', 'D')):
        raise ValueError('porta_h: argumentos invalidos.')

    if ld == 'E':
        tabuleiro_troca_celulas(tab, cria_coordenada(0, 0), cria_coordenada(1, 0))
        tabuleiro_troca_celulas(tab, cria_coordenada(1, 1), cria_coordenada(0, 1))
        tabuleiro_troca_celulas(tab, cria_coordenada(1, 2), cria_coordenada(0, 2))
    else:
        tabuleiro_troca_celulas(tab, cria_coordenada(2, 1), cria_coordenada(2, 2))
        tabuleiro_troca_celulas(tab, cria_coordenada(1, 1), cria_coordenada(1, 2))
        tabuleiro_troca_celulas(tab, cria_coordenada(0, 1), cria_coordenada(0, 2))

    return tab


def hello_quantum(s):
    """Uma funcao que permite ao utilizador jogar o jogo Hello Quantum.
    A funcao le o tabuleiro final de um ficheiro e pede input input das portas a aplicar ate do tabuleiro inicial se
    obter o tabuleiro final.

    Args:
        s (str): A string da qual le o tabuleiro e os movimentos minimos

    Returns:
        bool: True se o jogador obteu o tabuleiro lido do ficheiro no numero de jogadas minimo, False caso contrario

    Raises:
        ValueError: Se o jogador nao conseguir obter o tabuleiro final no numero de jogadas minimo.
    """
    tab_f = str_para_tabuleiro(s.split(':')[0])
    max_moves = int(s.split(':')[1])

    tab_i = tabuleiro_inicial()
    moves = 0

    print("Bem-vindo ao Hello Quantum!")
    print("O seu objetivo e chegar ao tabuleiro:")
    print(tabuleiro_para_str(tab_f))
    print("Comecando com o tabuleiro que se segue:")
    print(tabuleiro_para_str(tab_i))

    while not tabuleiros_iguais(tab_i, tab_f):
        if moves >= max_moves:
            return False

        prt = input("Escolha uma porta para aplicar (X, Z ou H): ")
        if not (prt in ['X', 'Z', 'H']):
            raise ValueError('hello_quantum: escolha invalida.')
        ld = input("Escolha um qubit para analisar (E ou D): ")
        if not (ld in ['E', 'D']):
            raise ValueError('hello_quantum: escolha invalida.')
        if prt == 'X':
            porta_x(tab_i, ld)
        elif prt == 'Z':
            porta_z(tab_i, ld)
        elif prt == 'H':
            porta_h(tab_i, ld)

        print(tabuleiro_para_str(tab_i))

        moves += 1

    print('Parabens, conseguiu converter o tabuleiro em', moves, "jogadas!")
    return True
