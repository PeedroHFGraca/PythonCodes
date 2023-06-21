def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()# substituir todas as virgulas por pontos
        if entrada.isalpha() or entrada == '':# se Entrada é numérico/ tirando os espaços de Entrada e não houver nada''
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)