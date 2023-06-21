def aumentar(n=0, taxa=0): # A 'taxa' é Parâmetro opcional
    res = n + (n * taxa/100)
    return res


def diminuir(n=0, taxa=0): # A 'taxa' é Parâmetro opcional
    res = n - (n * taxa/100)
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def moeda(n=0, moeda='R$'): # moeda função / moeda parâmetro
    return f'{moeda}{n:>8.2f}'.replace('.',',') # substituir todos pontos por vírgula
             # R$ / VALOR


