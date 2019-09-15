# Nome: Pedro Manuel Fernandez Godinho   Numero: 93608
def eh_tabuleiro(tab):
    """Uma funcao que retorna True se o argumento for um tuplo que representa um tabuleiro, False se nao o for.

    Considera-se um tabuleiro um tuple com 3 elementos:
    -Um primeiro tuple de 3 elementos;
    -Um segundo tuple de 3 elementos;
    -Um tuple de 2 elementos;
    Cada elemento desses tuples deve ser um inteiro entre -1 e 1.

    Args:
        tab (tuple): O tuplo a verificar

    Returns:
        bool: True caso o argumento seja um tabuleiro, False para qualquer outro argumento
    """
    if not (isinstance(tab, tuple) and len(tab) == 3):
        return False
    # Cada elemento deve ser um tuple de length 3 para indices 0 ou 1 ou length 2 para indice 3
    for idx, tup in enumerate(tab):
        if not (isinstance(tup, tuple) and ((len(tup) == 3 and idx < 2) or (len(tup) == 2 and idx == 2))):
            return False
        for cell in tup:
            if not (isinstance(cell, int) and -1 <= cell <= 1):
                return False
    return True


def tabuleiro_str(t):
    """Uma funcao que retorna uma representacao em string do tabuleiro dado.

    Args:
        t (tuple): O tabuleiro a transformar na sua representacao

    Returns:
        str: A representacao em string do argumento

    Raises:
        ValueError: Se o argumento nao for um tabuleiro
    """
    if not(eh_tabuleiro(t)):
        raise ValueError('tabuleiro_str: argumento invalido')

    # Um lambda para transformar uma celula na sua representacao string
    cell_str = lambda c: str(c) if (c == 1 or c == 0) else 'x'

    tab = '+-------+\n'
    tab += '|...{}...|\n'.format(cell_str(t[0][2]))
    tab += '|..{}.{}..|\n'.format(cell_str(t[0][1]), cell_str(t[1][2]))
    tab += '|.{}.{}.{}.|\n'.format(cell_str(t[0][0]), cell_str(t[1][1]), cell_str(t[2][1]))
    tab += '|..{}.{}..|\n'.format(cell_str(t[1][0]), cell_str(t[2][0]))
    tab += '+-------+'
    return tab


def tabuleiros_iguais(t1, t2):
    """Uma funcao que verifica a igualdade entre dois tabuleiros
    Consideram-se tabuleiros iguais dois tabuleiros em que todos os elementos sao iguais.

    Args:
        t1 (tuple): O primeiro tabuleiro
        t2 (tuple): O segundo tabuleiro

    Returns:
        bool: O valor de verdade da igualdade entre os dois tabuleiros

    Raises:
        ValueError: Se um dos argumentos nao for um tabuleiro
    """
    if not (eh_tabuleiro(t1) and eh_tabuleiro(t2)):
        raise ValueError('tabuleiros_iguais: um dos argumentos nao e tabuleiro')
    # A igualdade entre tuplos em python compara os elementos elemento a elemento por indice (significando tambem
    # que lengths diferentes implicam tuplos diferentes).
    # Como cada elemento e um tuplo, esses vao ser comparados elemento a elemento tambem.
    # Assim, a igualdade entre tuplos em python comporta-se como queremos para a funcao tabuleiros_iguais
    return t1 == t2


def porta_xy(porta, tabuleiro, lado):
    """Uma funcao que aplica a porta X ao tabuleiro passado no lado indicado.
    A funcao assume que os argumentos sao validos.

    Args:
        porta (str): Porta a aplicar. 'X' ou 'Z' para as portas X ou Z, respetivamente
        tabuleiro (tuple): Tabuleiro sobre o qual aplicar a porta
        lado (str): Lado sobre o qual aplicar a porta. 'E' ou 'D' para esquerda ou direita, respetivamente

    Returns:
        tuple: Um tabuleiro igual ao argumento t no qual foi aplicada a porta no lado indicado
    """

    # Um lamda para inverter uma celula do tabuleiro
    inverte_cell = lambda c: 0 if c == 1 else (1 if c == 0 else -1)

    line0 = ()
    line1 = ()
    line2 = ()

    if lado == 'E':
        # Caso o lado seja o esquerdo, basta iterar e inverter os valores da linha alterada pela porta em questao
        if porta == 'X':
            line0 = tabuleiro[0]
            line1 = tuple(inverte_cell(tabuleiro[1][i]) for i in range(len(tabuleiro[1])))
        else:
            line0 = tuple(inverte_cell(tabuleiro[0][i]) for i in range(len(tabuleiro[0])))
            line1 = tabuleiro[1]
        line2 += tabuleiro[2]
    elif lado == 'D':
        # nenhuma porta aplicada no lado direito altera o primeiro elemento das linhas 0 e 1
        line0 += (tabuleiro[0][0],)
        line1 += (tabuleiro[1][0],)
        if porta == 'X':
            # inverte-se o segundo elemento das linhas 0 e 1 e o primeiro da linha 2
            line0 += (inverte_cell(tabuleiro[0][1]),) + (tabuleiro[0][2],)
            line1 += (inverte_cell(tabuleiro[1][1]),) + (tabuleiro[1][2],)
            line2 += (inverte_cell(tabuleiro[2][0]),) + (tabuleiro[2][1],)
        else:
            # inverte-se o ultimo elemento das linhas 0, 1 e 2
            line0 += (tabuleiro[0][1],) + (inverte_cell(tabuleiro[0][2]),)
            line1 += (tabuleiro[1][1],) + (inverte_cell(tabuleiro[1][2]),)
            line2 += (tabuleiro[2][0],) + (inverte_cell(tabuleiro[2][1]),)

    return (line0,) + (line1,) + (line2,)


def porta_x(tabuleiro, lado):
    """Uma funcao que da uso a funcao porta(porta, tabuleiro, lado) para aplicar a porta X a um tabuleiro

        Args:
            tabuleiro (tuple): Tabuleiro sobre o qual aplicar a porta X
            lado (str): Lado sobre o qual aplicar a porta. 'E' ou 'D' para esquerda ou direita, respetivamente

        Returns:
            tuple: Um tabuleiro igual ao argumento t no qual foi aplicada a porta X no lado indicado

        Raises:
            ValueError: Se o primeiro argumento nao for um tabuleiro ou o segundo nao for uma string valida
    """
    if not (eh_tabuleiro(tabuleiro) and isinstance(lado, str) and (lado == 'E' or lado == 'D')):
        raise ValueError('porta_x: um dos argumentos e invalido')
    return porta_xy('X', tabuleiro, lado)


def porta_z(tabuleiro, lado):
    """Uma funcao que da uso a funcao porta(porta, tabuleiro, lado) para aplicar a porta Z a um tabuleiro

    Args:
        tabuleiro (tuple): Tabuleiro sobre o qual aplicar a porta Z
        lado (str): Lado sobre o qual aplicar a porta. 'E' ou 'D' para esquerda ou direita, respetivamente

    Returns:
        tuple: Um tabuleiro igual ao argumento t no qual foi aplicada a porta Z no lado indicado

    Raises:
        ValueError: Se o primeiro argumento nao for um tabuleiro ou o segundo nao for uma string valida
    """
    if not (eh_tabuleiro(tabuleiro) and isinstance(lado, str) and (lado == 'E' or lado == 'D')):
        raise ValueError('porta_z: um dos argumentos e invalido')
    return porta_xy('Z', tabuleiro, lado)


def porta_h(tabuleiro, lado):
    """Uma funcao que aplica a porta H sobre o tabuleiro t no lado l (esquerdo ou direito)

    Args:
        tabuleiro (tuple): Tabuleiro sobre o qual aplicar a porta H
        lado (str): Lado sobre o qual aplicar a porta. 'E' ou 'D' para esquerda ou direita, respetivamente

    Returns:
        tuple: Um tabuleiro igual ao argumento t no qual foi aplicada a porta H no lado indicado

    Raises:
        ValueError: Se o primeiro argumento nao for um tabuleiro ou o segundo nao for uma string valida
    """
    if not (eh_tabuleiro(tabuleiro) and isinstance(lado, str) and (lado == 'E' or lado == 'D')):
        raise ValueError('porta_h: um dos argumentos e invalido')

    line0 = ()
    line1 = ()
    line2 = ()

    if lado == 'E':
        # Aplicar a porta h no lado esquerdo implica apenas a troca das duas primeiras linhas
        line0 += tabuleiro[1]
        line1 += tabuleiro[0]
        line2 += tabuleiro[2]
    elif lado == 'D':
        # Aplicar a porta h no lado direido implica a troca dos dois ultimos elementos de cada linha
        line0 += (tabuleiro[0][0],) + (tabuleiro[0][2],) + (tabuleiro[0][1],)
        line1 += (tabuleiro[1][0],) + (tabuleiro[1][2],) + (tabuleiro[1][1],)
        line2 += (tabuleiro[2][1],) + (tabuleiro[2][0],)

    return (line0,) + (line1,) + (line2,)