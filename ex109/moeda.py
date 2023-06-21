def aumentar(n=0, taxa=0, formato=False):  # A 'taxa' é Parâmetro opcional
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)
    # Mostre o resultado normal ou formatado em moeda


def diminuir(n=0, taxa=0, formato=False):  # 'n' e 'taxa' é Parâmetro opcional
    res = n - (n * taxa / 100)
    return res if formato is False else moeda(res)
    # Mostre o resultado normal ou formatado em moeda


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)
    # Mostre o resultado normal ou formatado em moeda / igual ao primeiro


def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)
    # Mostre o resultado normal ou formatado em moeda


def moeda(n=0, moeda='R$'):  # moeda função / moeda parâmetro
    return f'{moeda}{n:>5.2f}'.replace('.', ',')  # substituir todos pontos por vírgula
             # R$ / VALOR

