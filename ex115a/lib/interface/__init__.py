def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[;31mErro! Tente usar números Inteiros válidos!\033[m')
        if ok:
            break
    return valor


def linha(tam=42): # linha com 42 caractéres
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[1mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f"\033[1;33m{c}\033[m - \033[1;34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaint('\033[1;33mSua opção: \033[m')
    return opc